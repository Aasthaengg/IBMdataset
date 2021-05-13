class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []
        self.size = 1
    
class UF:
    def __init__(self, size):
        self.n = size
        self.parents = [i for i in range(self.n+1)]
        self.sizes = [1] * (self.n+1)
        self.nodes = [None]
        for i in range(1, self.n+1):
            self.nodes.append(Node(i))
        

    def get_parent(self, x):
        while x.parent != None:
            x = x.parent
        return x

    def union(self, x, y):
        x = self.nodes[x]
        y = self.nodes[y]
        xp = self.get_parent(x)
        yp = self.get_parent(y)
        if xp == yp and xp is not None and yp is not None:
            return
        if xp.size >= yp.size:
            xp.children.append(yp)
            xp.size += yp.size
            self.sink(xp, yp)
        else:
            yp.children.append(xp)
            yp.size += xp.size
            self.sink(yp, xp)

    def sink(self, xp, yp):
        yp.parent = xp
        self.parents[yp.key] = xp.key
        yp.size = xp.size
        for child in yp.children:
            self.sink(xp, child)
            
from collections import defaultdict
n, k, l = map(int, raw_input().split())
uf1 = UF(n)
for i in range(k):
    p, q = map(int, raw_input().split())
    uf1.union(p, q)
uf2 = UF(n)
for i in range(l):
    r, s = map(int, raw_input().split())
    uf2.union(r, s)
p1 = uf1.parents
p2 = uf2.parents
dic = defaultdict(int)
for i in range(1, n+1):
    key = (p1[i], p2[i])
    dic[key] += 1
res_arr = []
for i in range(1, n+1):
    if uf1.nodes[i].size == 1 or uf2.nodes[i].size == 1:
        res_arr.append(1)
    else:
        key = (p1[i], p2[i])
        res_arr.append(dic[key])
print " ".join(map(str, res_arr))
