import os
import sys
from atexit import register
from io import BytesIO

import heapq

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
raw_input = lambda: sys.stdin.readline().rstrip('\r\n')

x,y,z,k = (int(x) for x in input().split())
a = sorted((int(i) for i in input().split()), reverse=True)
b = sorted((int(i) for i in input().split()), reverse=True)
c = sorted((int(i) for i in input().split()), reverse=True)


h = []
heapq.heappush(h, (-a[0]-b[0]-c[0],(0,0,0)))
visited = dict()
cnt = 0
while True:
    cost, node = heapq.heappop(h)
    if visited.get(node, False):
        continue
    visited[node] = True
    cnt += 1
    print(-cost)
    if cnt == k:
        break
    if node[0] + 1 != x:
        heapq.heappush(h,(cost+a[node[0]] - a[node[0] + 1], (node[0]+1, node[1], node[2])))
    if node[1] + 1 != y:
        heapq.heappush(h,(cost+b[node[1]] - b[node[1] + 1], (node[0], node[1]+1, node[2])))
    if node[2] + 1 != z:
        heapq.heappush(h,(cost+c[node[2]] - c[node[2] + 1], (node[0], node[1], node[2]+1)))
