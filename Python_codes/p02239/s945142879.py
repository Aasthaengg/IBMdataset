import sys
from collections import deque

inf = 1<<30

def solve():
    n = int(input())
    Adj = [None] * n

    for i in range(n):
        u, k, *line = [int(i) - 1 for i in input().split()]
        Adj[u] = line

    d = bfs(n, Adj)

    for i, di in enumerate(d, start=1):
        if di == inf:
            print(i, -1)
        else:
            print(i, di)

def bfs(n, Adj):
    d = [inf] * n
    d[0] = 0
    nxts = deque([0])

    while nxts:
        u = nxts.popleft()

        for v in Adj[u]:
            if d[v] == inf:
                d[v] = d[u] + 1
                nxts.append(v)

    return d

if __name__ == '__main__':
    solve()