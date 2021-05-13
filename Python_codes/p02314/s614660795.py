N, M = map(int, input().split())
Coins = list(map(int, input().split()))

DP = [10 ** 9 for _ in range(N + 1)]
DP[0] = 0

for i in range(N):
    for c in Coins:
        if i + c <= N:
            DP[i + c] = min(DP[i + c], DP[i] + 1)

print(DP[N])

