import collections

class WarshallFloyd():
    def __init__(self,N):  #Nは頂点の個数
        self.N = N
        self.d = [[float('inf')]*N for i in range(N)]  #d[i][j] = iからjへの最短距離,0-indexed
    def add(self,u,v,c,directed = False):
        if directed is False:  #無向グラフの場合
            self.d[u][v] = c
            self.d[v][u] = c
        else:  #有向グラフの場合
            self.d[u][v] = c
    def WarshallFloyd_search(self):
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.d[i][j] = min(self.d[i][j],self.d[i][k] + self.d[k][j])
        for i in range(self.N):
            self.d[i][i] = 0
        return self.d

H,W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(10)]
B = [list(map(int,input().split())) for i in range(H)]

G = WarshallFloyd(10)

for i in range(10):
    for j in range(10):
        G.add(i,j,A[i][j],directed=True)

d = G.WarshallFloyd_search()

C = []
for i in range(10):
    C.append(d[i][1])

D = [0]*11
for i in range(H):
    for j in range(W):
        if B[i][j] == -1:
            D[10] += 1
        else:
            D[B[i][j]] += 1

ans = 0
for i in range(10):
    ans += C[i]*D[i]

print(ans)