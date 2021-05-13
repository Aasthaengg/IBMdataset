"""
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
あ
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
みたな？































"""
import sys
input = sys.stdin.readline
N, K  = map(int, input().split())
e = [[] for _ in range(N + 1)]
mod = 10 ** 9 + 7
for _ in range(N - 1):
  u, v = map(int, input().split())
  e[u].append(v)
  e[v].append(u)

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

f = Factorial(N + K, mod)
s = [1]
vis = [0] * (N + 1)
res = f.permi(K, len(e[1]) + 1)
if K < len(e[1]) + 1: res = 0
while len(s):
  x = s.pop()
  vis[x] = 1
  for y in e[x]:
    if vis[y]: continue
    s.append(y)
    if K - 2 < 0 or (K - 2 < len(e[y]) - 1): res = 0
    res *= f.permi(K - 2, len(e[y]) - 1)
    res %= mod
print(res)