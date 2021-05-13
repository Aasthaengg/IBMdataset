class MergeFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n
        self.lista = [[_] for _ in range(n)]

    def find(self, a):
        to_update = []
        while a != self.parent[a]:
            to_update.append(a)
            a = self.parent[a]
        for b in to_update:
            self.parent[b] = a
        return self.parent[a]

    def merge(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.num_sets -= 1
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.lista[a] += self.lista[b]
        self.lista[b] = []

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


n,m=map(int,input().strip().split(" "))
ar=[]
for _ in range(m):
    ar.append((int(i) - 1 for i in input().strip().split(" ")))
ans=[]

d=MergeFind(n)

for i in range(m-1,-1,-1):
    a,b=ar[i]
    A=d.find(a)
    B=d.find(b)
    if A==B:
        ans.append(0)
    else:
        ans.append(d.size[A]*d.size[B])
        d.merge(a,b)
fin=[ans[-1]]
for i in range(m-2,-1,-1):
    fin.append(fin[-1]+ans[i])
for i in fin:
    print(i)

