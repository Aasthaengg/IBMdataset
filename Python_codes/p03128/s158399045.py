n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
cost = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1] * (n + 10)
dp[0] = 0

for i in range(n):
    for ai in a:
        if dp[i] >= 0:
            dp[i + cost[ai]] = dp[i] + 1

ans = []
i = n
while dp[i] > 0:
    for ai in a:
        if dp[i - cost[ai]] == dp[i] - 1:
            ans.append(str(ai))
            i -= cost[ai]
            break

print(''.join(ans))