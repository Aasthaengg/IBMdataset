n, m = map(int, input().split())

ps = list(map(int, input().split()))

par = [i for i in range(n)]
rank = [0]*n

def UnionFind(n):
    if par[n] == n:
        return n

    parent = par[n]
    par[n] = UnionFind(parent)
    return par[n]


def Unite(left, right):
    rootLeft = UnionFind(left)
    rootRight = UnionFind(right)
    if rootLeft != rootRight:
        if rank[rootRight] < rank[rootLeft]:
            par[rootRight] = rootLeft
        else:
            par[rootLeft] = rootRight
            if rank[rootLeft] == rank[rootRight]:
                rank[rootLeft] += 1



for i in range(m):
    a, b = (i-1 for i in map(int, input().split()))
    Unite(a, b)

sum = 0
for i, p in enumerate(ps):
    sourceRoot = UnionFind(i)
    targetRoot = UnionFind(p - 1)
    if sourceRoot == targetRoot:
       sum += 1

print(sum)

