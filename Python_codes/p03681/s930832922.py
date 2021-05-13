n, m = map(int, input().split())
mod = 10**9+7

if abs(n - m) >= 2:
   print(0)
   exit()

if n > m:
   n, m = m, n
ans = 1
for i in range(1, n+1):
   ans *= i
   ans %= mod

if n == m:
   print(2*pow(ans, 2, mod)%mod)
else:
   print(pow(ans, 2, mod)*m%mod)
