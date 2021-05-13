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

N,M=map(int,input().split())
G=UnionFind(N)
for i in range(M):
    a,b=map(int,input().split())
    G.unite(a-1,b-1)
D=dict()
for i in range(N):
    if G.find(i) in D:
        D[G.find(i)]+=1
    else:
        D[G.find(i)]=1
X=[]
for k in D:
    X.append(D[k])
print(max(X))
