class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parents = [-1] * N

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def all_group_members(self):
        dic = {}
        for x in range(self.N):
            r = self.find(x)
            dic.setdefault(r, [])
            dic[r].append(x)
        return dic

H,W=map(int, input().split())
S=[input() for _ in range(H)]
D=[1,0,-1,0,1]
UF=UnionFind(H*W)
for i in range(H):
    for j in range(W):
        for k in range(4):
            x=i+D[k]
            y=j+D[k+1]
            if 0<=x<H and 0<=y<W:
                if S[i][j]!=S[x][y]:
                    UF.union(x*W+y,i*W+j)
ans=0
for g in UF.all_group_members().values():
    w=0
    b=0
    for v in g:
        x,y=divmod(v,W)
        if S[x][y]=="#":
            b+=1
        else:
            w+=1
    ans+=w*b
print(ans)