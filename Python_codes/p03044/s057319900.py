import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
graph = [{} for _ in range(N)]

for _ in range(N-1):
    u, v, w = mapint()
    graph[u-1][v-1] = w%2
    graph[v-1][u-1] = w%2

from collections import deque
stack = deque([0])

colors = [-1]*N
colors[0] = 0
while stack:
    v = stack.pop()
    for nx in graph[v].keys():
        if colors[nx]==-1:
            w = graph[v][nx]
            colors[nx] = (colors[v]+w)%2
            stack.append(nx)

for a in colors:
    print(a)