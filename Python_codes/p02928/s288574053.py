n, k = map(int, input().split())

nums = [int(i) for i in input().split()]

mod = 10 ** 9 + 7

ans = 0
for i in range(n):
    c = 0
    for j in range(i + 1, n):
        if nums[i] > nums[j]:
            c += 1
    ans += (c * k) % mod

dp = [0] * n
for i in range(n):
    for j in range(n):
        if nums[i] > nums[j]:
            dp[i] += 1
for i in range(n):
    ans += ((k - 1) * k // 2 * dp[i]) % mod
print(ans % mod)