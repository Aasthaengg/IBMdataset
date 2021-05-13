n, k = map(int, input().split())
nums = [int(i) for i in input().split()]

mod = 10 ** 9 + 7 # (modの値をすごく大きくすれば（5乗とか）、普通のnCrとして使える)
MAX = 10 ** 5 + 1 # これは変動するので注意。せいぜい10 ** 6くらいまでがTLEの限界

def com_init(MAX, mod):
    fac = [0] * MAX
    finv = [0] * MAX
    inv = [0] * MAX
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    return fac, finv

fac, finv = com_init(MAX, mod)

def nCr(n, r):
    if n < r:
        return 0
    elif n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % mod) % mod

nums.sort()
MIN = 0
for i in range(n): #ここをkとして勘違いしていた。
    MIN += (nums[i] * nCr(n - i - 1, k - 1)) % mod

nums.sort(reverse=True)
MAX = 0
for i in range(n):
    MAX += (nums[i] * nCr(n - i - 1, k - 1)) % mod

ans = (MAX - MIN) % mod
print(ans)