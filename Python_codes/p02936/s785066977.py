import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

n,q = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(n-1):
    p,c = list(map(int, input().split()))
    graph[p].append(c)
    graph[c].append(p)

counter = defaultdict(int)
for _ in range(q):
    i,c = list(map(int, input().split()))
    counter[i] += c

ans = [0] * (n + 1)
visit = [False] * (n + 1)
def dfs(node, total_counter):
    visit[node] = True
    total_counter += counter.get(node, 0)
    
    for child in graph[node]:
        if not visit[child]:
            dfs(child, total_counter)
    ans[node] = total_counter

dfs(1, 0)

print(*ans[1:])