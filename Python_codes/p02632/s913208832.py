class comb():
  F = [1, 1]
  Fi = [1, 1]
  I = [0, 1]
  def __init__(self, num, mod):
    self.MOD = mod
    for i in range(2, num + 1):
      self.F.append((self.F[-1] * i) % mod)
      self.I.append(mod - self.I[mod % i] * (mod // i) % mod)
      self.Fi.append(self.Fi[-1] * self.I[i] % mod)
  def com(self, n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return self.F[n] * (self.Fi[k] * self.Fi[n - k] % self.MOD) % self.MOD


K = int(input())
S = input()
MOD = 10 ** 9 + 7

N = K + len(S)
M = len(S)
com = comb(N + 1, MOD)

p25 = [1]
for i in range(N + 1):
  p25.append(p25[-1] * 25 % MOD)

ans = 0

for i in range(K + 1):
  t = M + i
  ans = (ans + p25[N - t] * com.com(N, t)) % MOD

print(ans)
