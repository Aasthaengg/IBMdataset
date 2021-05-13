n,m=map(int,input().split())
ab=[list(map(int, input().split())) for _ in range(m)]

ab=ab[::-1]

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
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

    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())
        
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

uf = UnionFind(n) #初期化
result=[]
all_iland=n*(n-1)//2

for item in ab[0:-1]:
    a=item[0]-1
    b=item[1]-1
    if uf.same(a,b):
        i=1
    else:
        a_size=uf.size(a)
        b_size=uf.size(b)

        all_iland+=a_size*(a_size-1)//2+b_size*(b_size-1)//2
        uf.union(a,b)

        a_size=uf.size(a)
        all_iland-=a_size*(a_size-1)//2
    result.append(all_iland)


for item in result[::-1]:
    print(item)

print(n*(n-1)//2)






#uf.union(0, 2)#グループを併合
#uf.find(0) #親要素が変える




