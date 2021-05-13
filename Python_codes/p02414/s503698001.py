#coding: utf-8

n, m, l = (int(i) for i in input().split())
nm = [[0 for i in range(m)] for j in range(n)]
ml = [[0 for i in range(l)] for j in range(m)]
nl = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
    nm[i] = input().split()

for i in range(n):
    for j in range(m):
        nm[i][j] = int(nm[i][j])

for i in range(m):
    ml[i] = input().split()

for i in range(m):
    for j in range(l):
        ml[i][j] = int(ml[i][j])


for i in range(n):
    for j in range(l):
        for k in range(m):
            nl[i][j] += nm[i][k] * ml[k][j]

for i in range(n):
    for j in range(l):
        print(nl[i][j], end = ' ' if j != l-1 else '\n')
