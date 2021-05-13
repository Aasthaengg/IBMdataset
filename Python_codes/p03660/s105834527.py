# AtCoder Beginner Contest 067
# D - Fennec VS. Snuke
# https://atcoder.jp/contests/abc067/tasks/arc078_b
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
G = [[] for _ in [0]*N]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

# bfs
def bfs(s):
    q = deque()
    q.append(s)
    D = [0]*N
    visited = [False]*N
    while q:
        v = q.popleft()
        visited[v] = True
        d = D[v]

        for u in G[v]:
            if visited[u]:
                continue
            D[u] = d+1
            q.append(u)

    return D


Df = bfs(0)
Ds = bfs(N-1)

cnt_f = 0
cnt_s = 0
for df, ds in zip(Df, Ds):
    if df <= ds:
        cnt_f += 1
    else:
        cnt_s += 1

print('Fennec' if cnt_f > cnt_s else 'Snuke')
