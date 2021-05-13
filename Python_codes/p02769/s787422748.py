n, k = map(int, input().split())
Mod = 10**9+7

fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
def COMinit():
  #N_C_kのN
  for i in range(2, n+10):
    fac.append(fac[-1]*i%Mod)
    inv.append((-inv[Mod%i] * (Mod//i)) % Mod)
    finv.append(finv[-1] * inv[-1] % Mod)


def COM(n, k):
  if n < 0 or k < 0 or n < k:
    return 0
  return fac[n] * (finv[k] * finv[n-k] % Mod) % Mod


COMinit()
ans = 0
for i in range(min(n, k)+1):
  tmp = COM(n, i) % Mod
  tmp *= COM(i+n-i-1, i)
  tmp %= Mod
  ans += tmp
  ans %= Mod
print(ans)