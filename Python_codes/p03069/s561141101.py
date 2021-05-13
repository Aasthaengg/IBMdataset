N = int(input())
S = list(input())

cntW = 0
for s in S:
    if s == '.':
        cntW += 1

cntB = 0
MIN = 10 ** 5
for i in range(N+1):
    MIN = min(cntW+cntB,MIN)
    if i < N:
        if S[i] == '#':
            cntB += 1
        else:
            cntW -= 1

print(MIN)