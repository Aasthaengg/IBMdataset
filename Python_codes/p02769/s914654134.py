n, k = map(int, input().split())

# ①nCrの各項のmod(10^9+7)を事前計算
p = 10 ** 9 + 7
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, 2*n):
  fact.append((fact[-1] * i) % p)
  inv.append((-inv[p % i] * (p // i)) % p)
  factinv.append((factinv[-1] * inv[-1]) % p)

# ②事前計算した項を掛け合わせ
def cmb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  return fact[n] * factinv[r] * factinv[n-r] % p

rlt = 0
m = min(n,k+1)
for i in range(m):
  rlt += cmb(n-1,n-1-i,p)*cmb(n,i,p) % p
  rlt %= p
  
print(rlt)