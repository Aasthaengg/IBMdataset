import sys
input = sys.stdin.readline
N = int(input())
S = list(map(lambda x: ord(x) - ord("a"), list(input())[: -1]))

class BIT:
  def __init__(self, n):
    self.n = n
    self.data = [0] * (n + 1)
    self.el = [0] * (n + 1)
  def sum(self, i):
    s = 0
    while i > 0:
      s += self.data[i]
      i -= i & -i
    return s
  def add(self, i, x):
    self.el[i] += x
    while i <= self.n:
      self.data[i] += x
      i += i & -i
  def get(self, i, j = None):
    if j is None:
      return self.el[i]
    return self.sum(j) - self.sum(i)
  def lowerbound(self, s):
    x = 0
    y = 0
    for i in range(self.n.bit_length(), -1, -1):
      k = x + (1 << i)
      if k <= self.n and (y + self.data[k] < s):
        y += self.data[k]
        x += 1 << i
    return x + 1

fwk = [BIT(N) for _ in range(26)]
for i in range(N): fwk[S[i]].add(i + 1, 1)
for _ in range(int(input())):
  q, x, y = input().split()
  if q == "1":
    x = int(x)
    y = ord(y) - ord("a")
    fwk[S[x - 1]].add(x, -1)
    fwk[y].add(x, 1)
    S[x - 1] = y
  else:
    x = int(x)
    y = int(y)
    res = 0
    for i in range(26): res += fwk[i].get(x - 1, y) > 0
    print(res)