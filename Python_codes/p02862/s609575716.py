import math
X, Y = map(int, input().split())
      
def cmb(n, r, mod):
  if (r<0) or (n<r):
    return 0
  r = min(r, n-r)
  return (fac[n] * finv[r] * finv[n-r]) % mod

mod = 10**9+7
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
for i in range(2, (X+Y)//3+1):
  fac.append(fac[-1] * i % mod)
  inv.append(-inv[mod % i] * (mod // i) % mod)
  finv.append(finv[-1] * inv[-1] % mod)
  
ans = 0
x = 0
y = 0
if (X + Y) % 3 == 0:
  x = (2*Y-X) // 3
  y = (2*X-Y) // 3
  ans = cmb(x+y, x, mod)

print(ans)