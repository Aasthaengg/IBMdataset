import sys
input = sys.stdin.readline

from collections import deque

def getNeighbor(A, i):
    a = len(A)
    for k in range(2, a):
        M[i][A[k]-1] = 1

def bfs():
    u = q.popleft()
    c[u] = 1

    for v in range(n):
        if M[u][v] and c[v] == 0:
            q.append(v)
            d[v] = d[u] + 1
            c[v] = 1

    if q:
        bfs()

    return

    bfs()

q = deque([0])

n = int(input())
#color
c = [0] * n
d = [0] + [-1] * (n-1) #depth

M = [[0] * n for _ in range(n)]
t = 0

for i in range(n):
    A = list(map(int, input().split()))
    getNeighbor(A,i)

bfs()

for i in range(n):
    print(str(i+1), str(d[i]))


