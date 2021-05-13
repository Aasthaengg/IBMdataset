import copy
import sys

INF = 2**120

n = int(input())
d = [[] for j in range(n)]
for j in range(n):
    d[j] = [int(i) for i in input().split()]

ans = sum([sum(d[i]) for i in range(n)])

minus = [[0] * n for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k]+d[k][j]:
                print('-1')
                sys.exit()
            if d[i][j] == d[i][k]+d[k][j] and i != k and j != k:
                minus[i][j] = 1

for i in range(n):
    for j in range(n):
        if minus[i][j]:
            ans -= d[i][j]

print(ans//2)