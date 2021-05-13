mod = 10**9+7
n,k = map(int,input().split())
ans = 0
mod = 10**9 + 7
inv_t = [0,1]
for i in range(2,n+2):
  inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]
a = n
b = n-1
for i in range(1,min(n,k)+1):
    ans += a*b % mod
    a = a*(n-i)*inv_t[i+1] % mod
    b = b*(n-i-1)*inv_t[i+1] % mod
    ans %= mod
if k > 1:
    ans += 1
print(ans % mod)
