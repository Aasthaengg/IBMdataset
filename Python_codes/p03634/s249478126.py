import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
connected = [[]for _ in range(N+1)]
for i in range(N-1):
    a, b, c = (int(x) for x in input().split())
    connected[a].append((b,c))
    connected[b].append((a,c))
Q, K = (int(x) for x in input().split())
distk = [-1] * (N+1)
d = deque([K])
distk[K] = 0
while d:
    temp = d.popleft()
    for vert, dist in connected[temp]:
        if distk[vert] == -1:
            d.append(vert)
            distk[vert] = distk[temp] + dist
for i in range(Q):
    x, y = (int(x) for x in input().split())
    print(distk[x]+distk[y])