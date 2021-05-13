from collections import defaultdict
# d = defaultdict(int)で0で初期化
# d = defaultdict(lambda: 100)で100で初期化
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
n, m = map(int, input().split())
es = [defaultdict(int) for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    es[a][b] += 1
    es[b][a] += 1
    if es[a][b] == 2:
        es[a].pop(b)
        es[b].pop(a)

def dfs(v, p, r):
    for i in es[v]:
        if i != p:
            es[i].pop(v)
            es[v].pop(i)
            if i == r:
                return - 1
            else:
                return dfs(i, v, r)
    return - 2

for i in range(n):
    if es[i]:
        if dfs(i, -1, i) == -2:
            print("NO")
            exit()
print("YES")
        
