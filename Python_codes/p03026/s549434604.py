class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

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
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

n = int(input())
edge = []
for i in range(n-1):
    edge.append(list(map(int,input().split())))

c_arr = sorted(list(map(int,input().split())))

m = sum(c_arr) - max(c_arr)
ans = [0]*(n + 1)
a,b = edge.pop()
ans[a] = c_arr.pop()
ans[b] = c_arr.pop()
uf = UnionFind(n)
uf.union(a,b)
while edge:
    for i in range(len(edge)):
        if uf.same_check(a,edge[i][0]):
            if not uf.same_check(a,edge[i][1]):
                ans[edge[i][1]] = c_arr.pop()
                uf.union(edge[i][0],edge[i][1])
                edge.pop(i)
                break
        elif uf.same_check(a,edge[i][1]):
            ans[edge[i][0]] = c_arr.pop()
            uf.union(edge[i][0],edge[i][1])
            edge.pop(i)
            break
print(m)
print(*ans[1:])        
