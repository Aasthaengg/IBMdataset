from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)


n = int(input())
query = [[] for i in range(n)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    query[a-1].append((b-1, c))
    query[b-1].append((a-1, c))
q, k = map(int, input().split())
stack = deque([(k-1, 0, -1)])
dist = [0] * n
while stack:
    now, cnt, per = stack.pop()
    lis = query[now]
    dist[now] = cnt
    for nx, c in lis:
        if nx == per:
            continue
        if c != 0:
            stack.append((nx, cnt+c, now))
for i in range(q):
    x, y = map(int, input().split())
    print(dist[x-1] + dist[y-1])
