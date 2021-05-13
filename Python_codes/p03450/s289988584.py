import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
T = [[] for _ in range(N)]
for _ in range(M):
    l, r, d = map(int, input().split())
    T[l - 1].append((r - 1, d))
    T[r - 1].append((l - 1, -d))

Nvisited = set(range(N))
pos = dict()


def dfs(v):
    D = deque()
    D.append(v)
    pos[v] = 0
    while D:
        x = D.pop()
        for y, d in T[x]:
            if y in Nvisited:
                pos[y] = pos[x] + d
                Nvisited.remove(y)
                D.append(y)
            elif pos[y] - pos[x] != d:
                print('No')
                sys.exit()


while Nvisited:
    dfs(Nvisited.pop())

print('Yes')
