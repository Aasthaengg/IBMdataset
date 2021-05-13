from collections import defaultdict
import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 6)


@lru_cache(maxsize=None)
def rec(node):
    if len(graph[node]) == 0:
        return 0
    ans = 0
    for after in graph[node]:
        ans = max(ans, rec(after) + 1)
    return ans


n, m = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, rec(i))

print(ans)