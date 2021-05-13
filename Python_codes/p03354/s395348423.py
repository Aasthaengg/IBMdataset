n, m = map(int, input().split())
p = list(map(int, input().split()))

parent = [i + 1 for i in range(n)]
rank = [0 for i in range(n)]

def find(x):
    if parent[x - 1] == x:
        return x
    else:
        parent[x - 1] = find(parent[x - 1])
        return parent[x - 1]

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x - 1] < rank[y - 1]:
        parent[x - 1] = y
    else:
        parent[y - 1] = x
        if rank[x - 1] == rank[y - 1]:
            rank[x - 1] += 1

for i in range(m):
    x, y = map(int, input().split())
    unite(x, y)
dic = {}
for i in range(n):
    dic.setdefault(find(i + 1), [set(), set()])
    dic[find(i + 1)][0].add(i + 1)
    dic[find(i + 1)][1].add(p[i])
ans = 0
for i in dic.values():
    ans += len(i[0] & i[1])
print(ans)