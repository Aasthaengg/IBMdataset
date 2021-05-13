import sys
from collections import Counter
input = sys.stdin.readline
N, K = map(int, input().split())
if N == 1:
  print(K)
  exit(0)
elif N == 2:
  print(K * (K - 1))
  exit(0)
mod = 10 ** 9 + 7
e = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  u, v = map(int, input().split())
  e[u].append(v)
  e[v].append(u)

s = [1]
vis = [0] * (N + 1)
order = []
parent = [0] * (N + 1)
children = [0] * (N + 1)
while len(s):
  x = s.pop()
  vis[x] = 1
  order.append(x)
  for y in e[x]:
    if vis[y]: continue
    s.append(y)
    parent[y] = x
    children[x] += 1
cs = Counter()
cr = children[1]
for y in range(2, N + 1): cs[children[y]] += 1
#print(cs, cr)
res = [0] * (K + 1)
l = 0
csmx = 0
if len(cs): csmx = max(cs.keys())

for c in range(K + 1):
  if c <= 1 and (cr > 0): continue
  if c <= 2 and (len(cs) > 0): continue
  if c - 1 >= cr and (c - 2 >= csmx):
    l = c
    break
if l == 0:
  print(0)
  exit(0)

class Factorial:
  def __init__(self, n, mod):
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
    return self.f[n] * self.i[n - k] % mod * self.i[k] % mod

f = Factorial(K, mod)
smcs = sum(cs.values())
res[l] = f.factorial(l) * f.ifactorial(l - cr - 1) % mod
for k, v in cs.items():
  res[l] *= pow(f.factorial(l - 2) * f.ifactorial(l - k - 2) % mod, v, mod)
  res[l] %= mod
#print(res)
revs = [0] * (K + 1)
for i in range(K + 1): revs[i] = pow(i, mod - 2, mod)
for i in range(l, K):
  res[i + 1] = res[i] * pow(i - 1, smcs, mod) % mod
  res[i + 1] *= (i + 1) * revs[i - cr] % mod
  res[i + 1] %= mod
  for k, v in cs.items():
    res[i + 1] *= pow(revs[i - k - 1], v, mod)
    res[i + 1] %= mod
#print(res)
print(res[K])
"""
for _ in range(Q):
  x = int(input())
  print(res[x])
"""
