class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        # assert i > 0
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def get(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)

n = int(input())
s = list(input())
q = int(input())
ord_a = ord("a")
queries = [tuple(input().split()) for i in range(q)]
bits = [BIT(n) for i in range(26)]
for k,v in enumerate(s,1):
  bits[ord(v)-ord_a].add(k,1)
for query,i,c in queries:
  if query == "1":
    i = int(i)
    prev = s[i-1]
    if prev != c:
      bits[ord(prev)-ord_a].add(i,-1)
      bits[ord(c)-ord_a].add(i,1)
      s[i-1] = c
  elif query == "2":
    l,r = int(i),int(c)
    res = 0
    for bit in bits:
      if bit.get(r,l-1):
        res += 1
    print(res)