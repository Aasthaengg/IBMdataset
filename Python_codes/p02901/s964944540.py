N, M = map(int, input().split())
Cost = []
Key = []
for i in range(M):
    a, b = map(int, input().split())
    Cost.append(a)
    C_ = list(map(int, input().split()))
    C = 0
    for c in C_:
        C |= (1 << (c - 1))
    Key.append(C)
DP = [float('inf')] * (1 << N)
DP[0] = 0

for cost, key in zip(Cost, Key):
    D = DP[:]
    for i, d in enumerate(DP):
        if d == float('inf'):
            continue
        D[i|key] = min(D[i|key], d + cost)
    DP = D

if DP[-1] == float('inf'):
    print(-1)
else:
    print(DP[-1])

