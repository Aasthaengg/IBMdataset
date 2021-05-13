X, Y = map(int, input().split())

if (X+Y) % 3 != 0:
  print(0)
  exit()
if 2*X < Y or 2*Y < X:
  print(0)
  exit()
  
t = (X+Y)//3

# ①nCrの各項のmod(10^9+7)を事前計算
p = 10 ** 9 + 7
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, t + 1):
  fact.append((fact[-1] * i) % p)
  inv.append((-inv[p % i] * (p // i)) % p)
  factinv.append((factinv[-1] * inv[-1]) % p)

# ②事前計算した項を掛け合わせ
def cmb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  return fact[n] * factinv[r] * factinv[n-r] % p

print(cmb(t, X-t, p))