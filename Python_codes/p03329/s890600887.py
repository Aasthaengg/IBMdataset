N = int(input())
INF = 10 ** 9
dp = [INF] * (N + 1)
dp[0] = 0
M = set()
M.add(1)
i = 1
while True:
    if 6 ** i > N:
        break
    M.add(6 ** i)
    i += 1
i = 1
while True:
    if 9 ** i > N:
        break
    M.add(9 ** i)
    i += 1
for i in range(N):
    for m in M:
        if i + m > N:
            continue
        dp[i + m] = min(dp[i + m], dp[i] + 1)
print(dp[N])