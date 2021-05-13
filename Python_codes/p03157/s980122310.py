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
            #print(i,j,i,j)
            for k in range(4):
                ny = i + vy[k]
                nx = j + vx[k]
                if ny >= 0 and ny < h and nx >= 0 and nx < w:
                    #print(ny,nx)
                    if si[ny][nx] == '.':
                        #print(i,j,ny,nx)
                        #print(ki.same_check(i*w+j,ny*w+nx))
                        if ki.same_check(i*w+j,ny*w+nx) == True:
                            continue
                        #print(i,j,k)
                        ki.union(i*w+j,ny*w+nx)
                        #print(ki.par)
ans = 0
#exit()


#print(ki.size)
#print(ki.par)
li = [0]*(h*w+1)

for i in range(h):
    for j in range(w):
        #print(ki.find(i*w+j),1111111)
        ki.find(i*w+j)
        """
        if si[i][j] == '.':
            li[ki.find(i*w+h)] += 1
            print(ki.find(i*w+h))
        """
#print(ki.par)
for i in range(h):
    for j in range(w):
        if si[i][j] == '.':
            li[ki.par[i*w+j]] += 1
            #print(ki.par[i*w+h],ki.par)
#print(li)
#print(ki.par)

for i in range(h):
    for j in range(w):
        if si[i][j] == '#':
            #print(ki.size[i*w+j])
            #print(i,j)
            #tmp = 
            #print(ki.find(i*w+j))
            ans += li[ki.find(i*w+j)]
            #print(ans,i,j)
            
print(ans)