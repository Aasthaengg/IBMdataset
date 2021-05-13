N,M = list(map(int, input().split()))

LRs = [list(map(int, input().split())) for _ in range(M)]

L = []
R = []

for LR in LRs:
    L.append(LR[0])
    R.append(LR[1])

print(max(min(R) - max(L) + 1, 0))