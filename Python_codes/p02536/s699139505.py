import sys
def input():
	return sys.stdin.buffer.readline()[:-1]

class UnionFind():
	def __init__(self, size):
		self.table = [-1 for _ in range(size)]
		self.size = [1 for _ in range(size)]

	def find(self, x):
		while self.table[x] >= 0:
			if self.table[self.table[x]] >= 0:
				self.table[x] = self.table[self.table[x]]
			x = self.table[x]
		return x

	def unite(self, x, y):
		s1 = self.find(x)
		s2 = self.find(y)
		if s1 != s2:
			if self.table[s1] > self.table[s2]:
				self.table[s2] = s1
				self.table[s1] -= 1
				self.size[s1] += self.size[s2]
				self.size[s2] = 0
			else:
				self.table[s1] = s2
				self.table[s2] -= 1
				self.size[s2] += self.size[s1]
				self.size[s1] = 0
		return

n, m = map(int, input().split())
uf = UnionFind(n)
ans = n-1
for _ in range(m):
	a, b = map(int, input().split())
	if uf.find(a-1) != uf.find(b-1):
		ans -= 1
		uf.unite(a-1, b-1)

print(ans)