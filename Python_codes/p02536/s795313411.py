import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
table = [[] for i in range(N)]
Q = deque()
visited = [0]*N
ans = 0
for i in range(M):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    table[A].append(B)
    table[B].append(A)

for x in range(N):
    if visited[x] == 0:
        ans += 1
        Q.append(x)
        while Q:
            x = Q.popleft()
            for y in table[x]:
                if visited[y]==0:
                    Q.append(y)
                    visited[y] = 1

print(ans-1)