N = int(input())
F = [tuple(map(int, input().split())) for _ in range(N)]

DP = [0] * 3

for f in F:
    D = [0] * 3
    S = {0, 1, 2}
    for i in range(3):
        S.remove(i)
        for s in S:
            D[i] = max(D[i], f[i] + DP[s])
        S.add(i)
    DP = D

print(max(DP))