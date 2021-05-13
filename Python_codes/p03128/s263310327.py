n, m = map(int, input().split())
aa = reversed(sorted(map(int, input().split())))

t = ['_', 2, 5, 5, 4, 5, 6, 3, 7, 6]

# n 本使ってできる最大の桁数
dp = [-1 for _ in range(n + 1)]
dp[0] = 0

for a in aa:
    for i in range(len(dp)):
        if dp[i] >= 0 and i + t[a] < len(dp):
            dp[i + t[a]] = max(dp[i + t[a]], dp[i] * 10 + a)

print(dp[n])
