import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
query = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = mapint()
    query[a-1].append((b-1, c))
    query[b-1].append((a-1, c))

Q, K = mapint()
from collections import deque
stack = deque([(K-1, 0, -1)])
dist = [0]*N
while stack:
    now, cnt, per = stack.pop()
    lis = query[now]
    dist[now] = cnt
    for nx, c in lis:
        if nx==per:
            continue
        if c!=0:
            stack.append((nx, cnt+c, now))

for _ in range(Q):
    x, y = mapint()
    print(dist[x-1]+dist[y-1])