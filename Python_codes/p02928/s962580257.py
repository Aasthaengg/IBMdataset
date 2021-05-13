n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
mod = 10**9+7

lower = [0]*n
tento = [0]*n
for i in range(n):
    t = a[i]
    for j in range(n):
        if t > a[j]:
            lower[i] += 1
            if j > i:
                tento[i] += 1
for i in range(n):
    ans += k*tento[i] % mod
    ans += (k-1)*k*lower[i]//2 % mod
print(ans%mod)
