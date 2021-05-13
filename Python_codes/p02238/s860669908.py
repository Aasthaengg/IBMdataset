import sys
input = sys.stdin.readline

from collections import deque

S = deque([])

def getNeighbor(A, i):
    a = len(A)
    for k in range(2, a):
        M[i][A[k]-1] = 1


def dfs(u):
    global t
    t = t + 1
    S.append(u)
    c[u] = 1
    d[u] = t

    for v in range(n):
        if M[u][v] and c[v] == 0:
            dfs(v)
    c[u] = 2
    t += 1
    f[u] = t


n = int(input())
#color
c = [0] * n
d = [0] * n
f = [0] * n

M = [[0] * n for _ in range(n)]
t = 0

for i in range(n):
    A = list(map(int, input().split()))
    getNeighbor(A,i)

for num in range(n):
    if d[num] == 0:
        dfs(num)

for i in range(n):
    print(str(i+1), str(d[i]), str(f[i]))








