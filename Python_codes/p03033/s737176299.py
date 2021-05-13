import sys
input = sys.stdin.readline
n, q = map(int,input().split())
S = [list(map(int,input().split())) for i in range(n)]
D = [int(input()) for i in range(q)]

A = []
for i in range(n):
    s = S[i][0]
    t = S[i][1]
    x = S[i][2]
    A.append([s-x-0.5, x, i, 0])
    A.append([t-x-0.5, x, i, 1])
for i in range(q):
    A.append([D[i], 0, 0, 2])

A.sort()
from heapq import heappop, heappush
Q = []
F = [0] * n
for i in range(len(A)):
    s = A[i][0]
    x = A[i][1]
    j = A[i][2]
    f = A[i][3]
    if f == 0:
        heappush(Q, [x, j])
        F[j] = 1
    elif f == 1:
        F[j] = 0
    elif f == 2:
        while len(Q) > 0 and F[Q[0][1]] == 0:
            heappop(Q)
        if len(Q) > 0:
            print(Q[0][0])
        else:
            print(-1)
