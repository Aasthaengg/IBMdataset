s = "0" + input()
n = len(s)
S = []
for i in range(n-1,-1,-1):
    S.append(int(s[i]))

ans = sum(S)
ans0 = ans
D = [[0] * 3 for i in range(n)]
D[0] = [S[0], S[0]+1, 10-S[0]]
for i in range(1, n):
    D[i][0] = min(D[i-1][0], D[i-1][1]) + S[i]
    D[i][1] = D[i-1][2] + S[i] + 1
    D[i][2] = min(D[i-1][0]+10-S[i], D[i-1][1]+10-S[i], D[i-1][2]+9-S[i])

# print(D)
print(min(D[-1][:2]))
