MOD = 10**9+7
a = 10**6
n, k = map(int, input().split())
nums = [i for i in range(n+1)]
min_n = sum(nums[:k])
max_n = sum(nums[-k:])
res = (max_n-min_n)+1
res %= MOD
i = 0
while k+i <= n:
    min_n += nums[k+i]
    max_n += nums[-(k+i+1)]
    diff = max_n - min_n
    res += diff+1
    res %= MOD
    i += 1

print(res)
