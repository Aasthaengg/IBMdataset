class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if(x == y):
            return
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        return -self.root[self.Find_Root(x)]


n, m = map(int, input().split())
ab = []
for i in range(m):
    a, b = map(int, input().split())
    ab.append([a, b])

all_ptn = n * (n - 1) // 2
num = 0
ret = [str(all_ptn)]

uni = UnionFind(n)
for i in range(1, m):
    a, b = ab[-i]
    prev_a = uni.Count(a)
    prev_b = uni.Count(b)
    if not uni.isSameGroup(a, b):
        uni.Unite(a, b)
        now_ab = uni.Count(a)
        cnt = now_ab * (now_ab - 1) // 2 - (prev_a * (prev_a - 1)) // 2 - \
            (prev_b * (prev_b - 1)) // 2
        num += cnt
    ret.append(str(all_ptn - num))

ret.reverse()

print('\n'.join(ret))
