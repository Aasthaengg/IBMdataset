from collections import deque
class UnionFind:
    """
        n : 要素数
        root : 親ノード
        size : グループのサイズ
    """
    
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.size = [1]*(n+1)
    
    """ノードxのrootノードを見つける"""
    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    
    """木の合併"""
    def Union(self, x, y):
        #入力ノードの親を探索
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        
        #既に同じ木に所属する場合
        if x==y:
            return 
        
        #異なる木に所属する場合 -> sizeが小さい方から大きい方に合併する
        elif self.size[x] > self.size[y]:
            self.size[x] += self.size[y]
            self.root[y] = x
        
        else:
            self.size[y] += self.size[x]
            self.root[x] = y

n = int(input())
uf = UnionFind(n)
G = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    uf.Union(a,b)
    G[a].append(b)
    G[b].append(a)
rt = uf.root.index(-1)
for idx in range(1, n+1):
    if uf.root[idx] == -1:
        rt = idx-1
        break

c = list(map(int,input().split()))
c.sort(reverse=True)
c = [0] + c
ans = [0]*(n+1)
que = deque([rt])
idx = 1

while que:
    node = que.popleft()
    if ans[node]!=0:
        continue
    else:
        ans[node] = c[idx]
        idx += 1
        for g in G[node]:
            que.append(g)
print(sum(c)-max(c))
print(*ans[1:])