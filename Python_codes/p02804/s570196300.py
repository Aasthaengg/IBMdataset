import sys
input = sys.stdin.readline
N, K = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
a.sort()

class Factorial:
  def __init__(self, n, mod):
    self.mod = mod
    self.f = [1]
    for i in range(1, n + 1):
      self.f.append(self.f[-1] * i % mod)
    self.i = [pow(self.f[-1], mod - 2, mod)]
    for i in range(1, n + 1)[: : -1]:
      self.i.append(self.i[-1] * i % mod)
    self.i.reverse()
  def factorial(self, i):
    return self.f[i]
  def ifactorial(self, i):
    return self.i[i]
  def combi(self, n, k):
    return self.f[n] * self.i[n - k] % self.mod * self.i[k] % self.mod
  def permi(self, n, k):
    return self.f[n] * self.i[n - k] % self.mod

f = Factorial(N, mod)

res = 0
for l in range(N - K + 1):
  res -= f.combi(N - l - 1, K - 1) * a[l]
  res %= mod
for r in range(K - 1, N):
  res += f.combi(r, K - 1) * a[r]
  res %= mod
print(res)
