#!/usr/bin/python3

def find(A, id, V, time):
    i = id - 1
    A[i][0] = True
    A[i][1] = time
    time += 1
    for v in V[i]:
        if A[v - 1][0] == False:
            time = find(A, v, V, time)
    A[i][2] = time
    time += 1
    return time

n = int(input())
# [isFind, d, f]
A = [[False, 0, 0] for i in range(n)]
U = []
V = []
for i in range(n):
    l = list(map(int, input().split()))
    U.append(l[0])
    V.append(l[2:])

time = 1
for u in U:
    if A[u - 1][0] == False:
        time = find(A, u, V, time)

for u in U:
    l = [u]
    l.extend(A[u - 1][1:])
    print(' '.join(map(str, l)))