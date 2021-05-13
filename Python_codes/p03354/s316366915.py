# Union Find
# xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


# xとyの属する集合の併合
def unite(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        # x < y にする
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x
        return True


# xとyが同じ集合に属するかの判定
def same(x, y):
    return find(x) == find(y)


n, m = map(int, input().split())
par = [-1] * n

l = list(map(int, input().split()))

for _ in range(m):
    x, y = map(int, input().split())
    unite(x - 1, y - 1)

print(sum(same(i, l[i] - 1) for i in range(n)))