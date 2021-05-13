mod = 998244353
n, k = map(int, input().split())
index_list = []
for _ in range(k):
    l, r = map(int, input().split())
    index_list.append([l, r])

dp = [0 for _ in range(n)]
dpsum = [0 for _ in range(n)]
dp[0] = 1
dpsum[0] = 1
for i in range(1, n):
    for l, r in index_list:
        l_index = max(i - r - 1, -1)
        r_index = i - l
        if r_index >= 0:
            dp[i] += dpsum[r_index]
            if (r_index > l_index) & (l_index >= 0):
                dp[i] -= dpsum[l_index]
    dp[i] = dp[i] % mod
    dpsum[i] = (dp[i] + dpsum[i - 1]) % mod
print(dp[-1])