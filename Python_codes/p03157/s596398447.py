h,w = map(int,input().split())
si = [input() for i in range(h)]

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1 for _ in range(n+1)]
 
    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
 
    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
 
    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
    
ki = UnionFind(h*w)

vx = [0,1,0,-1]
vy = [1,0,-1,0]

for i in range(h):
    for j in range(w):
        if si[i][j] == '#':
            for k in range(4):
                ny = i + vy[k]
                nx = j + vx[k]
                if ny >= 0 and ny < h and nx >= 0 and nx < w:
                    if si[ny][nx] == '.':
                        if ki.same_check(i*w+j,ny*w+nx) == True:
                            continue
                        ki.union(i*w+j,ny*w+nx)
ans = 0

li = [0]*(h*w+1)

for i in range(h):
    for j in range(w):
        if si[i][j] == '.':
            li[ki.find(i*w+j)] += 1

for i in range(h):
    for j in range(w):
        if si[i][j] == '#':
            ans += li[ki.find(i*w+j)]
            
print(ans)