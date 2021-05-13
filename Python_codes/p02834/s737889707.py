'''input
3 5
1 2 1
2 3 0
'''
# connected components
from sys import stdin, setrecursionlimit
from bisect import bisect_left
import sys, threading
from collections import defaultdict
sys.setrecursionlimit(10 ** 5 + 1)

def dfs(node, distance, graph, visited, cur):
    visited[node] = True
    distance[node] = cur
    for i in graph[node]:
        if i not in visited:
            dfs(i, distance, graph, visited, cur + 1)


# main start
n, T, A = list(map(int, stdin.readline().split()))
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = list(map(int, stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)

T_traverse = [0] * (n + 1)
A_traverse = [0] * (n + 1)
visited = dict()
dfs(T, T_traverse, graph, visited, 0)
visited = dict()
dfs(A, A_traverse, graph, visited, 0)
# print(T_traverse)
# print(A_traverse)
ans = 0
for i in range(1, n + 1):
    if T_traverse[i] <= A_traverse[i]:
        diff = A_traverse[i] - T_traverse[i]
        if diff % 2 == 0:
            for adj in graph[i]:
                if A_traverse[adj] > A_traverse[i] - 1:
                    ans = max(ans, A_traverse[i])
                    break
            else:
                ans = max(ans, A_traverse[i] - 2)
        else:
            ans = max(ans, A_traverse[i] - 1)
print(ans)
