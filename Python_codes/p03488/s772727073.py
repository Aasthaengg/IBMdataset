s = input()
x, y = map(int, input().split())
n = len(s)

D = [[], []]
st_x = 0
st_y = 0
st = 0
while st <= len(s)-1 and s[st] == "F":
    x -= 1
    st += 1

di = 0
for i in range(st, n):
    if s[i] == "T":
        di = (di+1) % 2
        D[di].append(0)
    else:
        D[di][-1] += 1

# print(D)


ANS = [0, 0]
st_po = [0, 0]
go_po = [x, y]
for i in range(2):
    mid = sum(D[i]) + 5
    DP = [[0] * (mid*2) for i in range(len(D[i]) + 1)]
    DP[0][st_po[i] + mid] = 1
    for j in range(len(D[i])):
        dd = D[i][j]
        for k in range(len(DP[0])):
            aa = 0
            bb = 0
            if 0 <= k-dd <= len(DP[0])-1:
                aa = DP[j][k-dd]
            if 0 <= k+dd <= len(DP[0])-1:
                bb = DP[j][k+dd]

            DP[j+1][k] = int(aa or bb)

    if 0 <= go_po[i]+mid <= len(DP[0])-1:
        ANS[i] = DP[-1][go_po[i]+mid]
    # print("len",mid*2)
    #if i == 1:
        # print(DP[1][7999+mid])
# print(ANS)

print("Yes" if ANS[0] and ANS[1] else "No")