class Unionfind():
    
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x==y:
            return 

        if self.parents[x]>self.parents[y]:
            x,y = y,x
        
        self.parents[x]+=self.parents[y]
        self.parents[y]= x

    def size(self, x):
        return -self.parents[self.find[x]]
    
    def same(self, x, y):
        return self.find(x)==self.find(y)

    def members(self, x):
        root = self.find(x)
        return [ i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [ i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __ser__(self):
        return '\n'.join('{}: {}'.format(r, sself.members(r)) for r in self.roots())

n,k,l = map(int, input().split())
a = Unionfind(n)
b = Unionfind(n)
for i in range(k):
    p,q = map(int, input().split())
    p -=1
    q -=1
    a.union(p,q)

for i in range(l):
    r,s = map(int, input().split())
    r-=1
    s-=1
    b.union(r,s)

c = [(a.find(x),b.find(x)) for x in range(n)]
count = {}
for i in c:
    if i in count:
        count[i]+=1
    else:
        count[i] = 1
print(*[count[i] for i in c])