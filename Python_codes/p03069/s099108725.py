N = int(input())
S = input()
lS = len(S)
l = 0
bw = [0, 0]
for i in range(lS):
    if (S[i] == "."):
        bw[1] += 1

ans = sum(bw)
for i in range(lS):
    if (S[i] == "#"):
        bw[0] += 1
    if (S[i] == "."):
        bw[1] -= 1

    if (ans > sum(bw)):
        ans = sum(bw)

print(ans)
