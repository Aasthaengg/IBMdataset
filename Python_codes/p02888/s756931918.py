# Binary Indexed Tree (Fenwick Tree)
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


N = int(input())
L = list(map(int, input().split()))
L.sort()
bit = BIT(L[-1]*2+1)
bit.add(L[0]+L[1], 1)
total = 1
ans = 0
for k in range(2, N):
  ans += total - bit.sum(L[k])
  for j in range(k):
    bit.add(L[j]+L[k], 1)
    total += 1

print(ans)  
