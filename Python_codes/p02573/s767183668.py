n, m = map(int, input().split())
groups = [x for x in range(n)]
count = [0]*n

def UnionFind(x):
    a = x
    while a != groups[a]:
        a = groups[a]
    groups[x] = a
    return a

for _ in range(m):
    x, y = map(int, input().split())
    x, y = UnionFind(x-1), UnionFind(y-1)
    if x != y:
        groups[y] = x
    
for i in range(n):
    count[UnionFind(i)] += 1
print(max(count))