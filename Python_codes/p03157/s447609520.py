class UnionFind():
    n=1
    par=[0]
    rnk=[0]
    def __init__(self,size):
        self.n=size
        self.par=[i for i in range(self.n)]
        self.rnk=[0 for i in range(self.n)]
    def find(self,vertex1):
        if self.par[vertex1]==vertex1:
            return vertex1
        else:
            self.par[vertex1]=self.find(self.par[vertex1])
            return self.par[vertex1]
    def unite(self,vertex1,vertex2):
        vertex1=self.find(vertex1)
        vertex2=self.find(vertex2)
        if vertex1==vertex2:
            return
        if (self.rnk[vertex1]<self.rnk[vertex2]):
            self.par[vertex1]=vertex2
        else:
            self.par[vertex2]=vertex1
            if(self.rnk[vertex1]==self.rnk[vertex2]):
                self.rnk[vertex1]+=1
    def same(self,vetrex1,vertex2):
        return self.find(vetrex1)==self.find(vertex2)
H,W=map(int,input().split())
S=[list(input()) for i in range(H)]
G=UnionFind(H*W)
#i*W+j
for i in range(H):
    for j in range(W-1):
        if S[i][j]!=S[i][j+1]:
            G.unite(i*W+j,i*W+(j+1))
for i in range(H-1):
    for j in range(W):
        if S[i][j]!=S[i+1][j]:
            G.unite(i*W+j,(i+1)*W+j)
D=dict()
for i in range(H):
    for j in range(W):
        k=G.find(i*W+j)
        if not k in D:
            D[k]=[0,0]
        if S[i][j]=="#":
            D[k][0]+=1
        else:
            D[k][1]+=1
ans=0
for k in D:
    x=D[k][0]
    y=D[k][1]
    ans+=x*y
print(ans)
