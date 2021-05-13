class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
        
    def find_root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]
        
    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1
                
    def isSameGroup(self, x, y):
        return self.find_root(x) == self.find_root(y)
    
    def count(self, x):
        return -self.root[self.find_root(x)]


N,K,L = map(int, input().split())
road_list = []
for i in range(K):
    road_list.append([int(x) for x in input().split()])
train_list = []
for i in range(L):
    train_list.append([int(x) for x in input().split()])
    
road = UnionFind(N)
train = UnionFind(N)

for i in range(K):
    road.unite(road_list[i][0], road_list[i][1])
    
for i in range(L):
    train.unite(train_list[i][0], train_list[i][1])
    
R = [i for i in range(N+1)]
T = [i for i in range(N+1)]

for i in range(1, N+1):
    R[i] = road.find_root(i)
    T[i] = train.find_root(i)
    
pair = [0 for i in range(N+1)]
for i in range(1, N+1):
    pair[i] = (R[i], T[i])
    
dic = {}
for i in range(1, N+1):
    if pair[i] in dic:
        dic[pair[i]] += 1
    else:
        dic[pair[i]] = 1
        
for i in range(1, N+1):
    print(dic[pair[i]])