import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
G = [list(map(lambda x: int(x)-1, input().split()))[2:] for _ in range(N)]

D = [-1]*N
q = deque([[0, 0]])
while q:
    cur, dis = q.popleft()
    if D[cur] != -1: continue
    D[cur] = dis
    for nex in G[cur]:
        q.append([nex,dis+1])
for i in range(N):
    print(i+1, D[i])

