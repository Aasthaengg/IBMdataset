n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10**9+7

ans = 0
y01 = (y[1] - y[0])%mod
ynum = m-1
for i in range(n-1):
    s = (((x[i+1] - x[i])%mod) * y01) % mod
    xnum = (i+1) * (n-i-1)
    ans = (ans + (s*xnum*ynum) % mod) % mod
band = ans

inv = [0] * (m + 1)
inv[1] = 1
for i in range(2, m):
    inv[i] = mod - inv[mod % i] * (mod // i) % mod

for j in range(1, m-1):
    band = (((((band * inv[j])%mod) * inv[m-j])%mod) * (((j+1) * (m-j-1))%mod))%mod
    band = ((band * ((y[j+1] - y[j])%mod))%mod * pow(((y[j]-y[j-1])%mod), mod-2, mod))%mod
    ans = (ans + band)%mod

print(ans)
