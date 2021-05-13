N = int(input())
S = list(input())

rightWhite = []
leftBlack = []

cntB = 0
cntW = 0

for i in range(N):
    rightWhite.append(cntW)
    leftBlack.append(cntB)
    if (S[i] == "#"):
        cntB += 1

    if (S[-i-1] == "."):
        cntW += 1

rightWhite = list(reversed(rightWhite))

ans = N

for i in range(N):
    ans = min(rightWhite[i] + leftBlack[i], ans)

print(ans)
