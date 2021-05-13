n,m = list(map(int, input().split()))
p = list(map(int, input().split()))

# parentsには根の要素番号（自身が根の場合は、要素数（マイナスの値））が入る
parents = [-1] * (n + 1)
def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parents[x] > parents[y]:
        x, y = y, x

    parents[x] += parents[y]
    parents[y] = x

def same(x, y):
    return find(x) == find(y)

for _ in range(m):
    x,y = list(map(int, input().split()))
    union(x,y)

# 同じグループ内では好きに入れ替えられる
ans = 0
for i,P in enumerate(p, 1):
    if i == P or same(i, P):
        ans += 1

print(ans)