import sys
import collections as c
sys.setrecursionlimit(10**6)

import sys
sys.setrecursionlimit(10**7)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        return -self.root[self.Find_Root(x)]

N, K, L = map(int,input().split())
p = []
q = []
l = []
r = []

for _ in range(K):
	p_tmp, q_tmp = map(int ,input().split())
	p.append(p_tmp)
	q.append(q_tmp)

for _ in range(L):
	l_tmp, r_tmp = map(int, input().split())
	l.append(l_tmp)
	r.append(r_tmp)

road = UnionFind(N)
train = UnionFind(N)

for i in range(K):
	road.Unite(p[i], q[i])

for i in range(L):
	train.Unite(l[i], r[i])

ar = []

for i in range(1,N+1):
	a = road.Find_Root(i)
	b = train.Find_Root(i)
	ar.append(str([a,b]))

Car = c.Counter(ar)

for i in range(N):
	print(Car[ar[i]], end = " ")