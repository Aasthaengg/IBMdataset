import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
road = []
train = []
for i in range(k):
    road.append(list(map(int, input().split())))
for i in range(l):
    train.append(list(map(int, input().split())))

class Union_Find():
    def __init__(self, num):
        self.par = [-1]*(num+1)
        self.siz = [1]*(num+1)

    def same_checker(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            x = self.par[x]
            return self.find(x)

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] < self.par[ry]:
                self.par[ry] = rx
                self.siz[rx] += self.siz[ry]
            elif self.par[rx] > self.par[ry]:
                self.par[rx] = ry
                self.siz[ry] += self.siz[rx]
            else:
                self.par[rx] -= 1
                self.par[ry] = rx
                self.siz[rx] += self.siz[ry]
        return

    def size(self, x):
        return self.siz[self.find(x)]

road_root = Union_Find(n)
train_root = Union_Find(n)
for i in range(k):
    road_root.union(road[i][0], road[i][1])
for i in range(l):
    train_root.union(train[i][0], train[i][1])

road = []
train = []
for i in range(n):
    road.append(road_root.find(i+1))
    train.append(train_root.find(i+1))

road
train

pair = []
for i in range(n):
    pair.append((road[i], train[i]))

d = dict()
for i in range(n):
    if pair[i] not in d:
        d[pair[i]] = 1
    else:
        d[pair[i]] += 1

ans = []
for i in range(n):
    ans.append(d[pair[i]])

print(" ".join(map(str, ans)))
