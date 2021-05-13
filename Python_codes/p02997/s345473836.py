from itertools import combinations
n, k = map(int, input().split())
if k>(n-1)*(n-2)//2:
    print(-1)
    exit(0)
edges = []
for i in range(2, n+1):
    edges.append((1, i))
k = (n-1)*(n-2)//2-k
for i, j in combinations(range(2, n+1), 2):
    if k==0:
        break
    edges.append((i, j))
    k -= 1
print(len(edges))
for i, j in edges:
    print(i, j)