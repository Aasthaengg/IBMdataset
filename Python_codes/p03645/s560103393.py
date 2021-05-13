n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

for first in g[0]:
    if n-1 in g[first]:
        print("POSSIBLE")
        exit()
else:
    print("IMPOSSIBLE")
