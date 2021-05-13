import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    x, y = list(map(lambda x: int(x)-1, input().split()))
    edges[x].append(y)

dist = [-1]*n


def longest_path(v):
    if dist[v] != -1:
        return dist[v]
    retval = 0
    for v2 in edges[v]:
        retval = max(retval, longest_path(v2)+1)
    dist[v] = retval
    return dist[v]


ans = 0
for i in range(n):
    ans = max(ans, longest_path(i))
print(ans)