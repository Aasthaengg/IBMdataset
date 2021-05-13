import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
'''
N, M = mi()
P = li()
tmp = []


for i in range(M):
    x, y = mi()
    x, y = x-1, y-1
    if x > y:
        x, y = y, x
    tmp.append([x, y])

xy = []

sorted(tmp, key=lambda x : x[0])
print(tmp)
now = tmp[0][0]
flag = [0] * N
tmp2 = [now]
num = 1
flag[tmp[0][0]] = num
for x, y in tmp:
    if x != now:
        xy.append(tmp2)
        tmp2 = [x]
        now = x
        num += 1
        flag[x] = num
    tmp2.append(y)
    flag[y] = num

if tmp2:
    xy.append(tmp2)

print(flag)
print(xy)

for i in range(N):
'''
class UnionFind:
    def __init__(self, n):
        self.d = [-1]*n
    
    def find(self, x):
        if self.d[x] < 0:
            return x
        else:
            self.d[x] = self.find(self.d[x])
            return self.find(self.d[x])
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return False
        if self.d[x] > self.d[y]:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True
    
    def same(self, x, y):
        if self.find(x)==self.find(y):
            return True
        return False
    
    def size(self, x):
        return (-1) * self.d[self.find(x)]

N, M = mi()
P = li()
G = UnionFind(N)
ans = 0

for i in range(M):
    x, y = mi()
    G.unite(x-1, y-1)
    
for i in range(N):
    if G.same(P[i]-1, i):
        ans += 1

print(ans)
    



