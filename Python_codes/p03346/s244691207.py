N = int(input())
P = [int(input()) for _ in range(N)]
DP = [0] * (N + 1)

for p in P:
    DP[p] = DP[p-1] + 1

print(N - max(DP))

