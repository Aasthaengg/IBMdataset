# from pprint import pprint
# import math
# import collections

# n = int(input())
n, m = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))
a, b = [], []
for i in range(n):
    _a, _b = map(int, input().split(' '))
    a.append(_a)
    b.append(_b)
c, d = [], []
for i in range(m):
    _c, _d = map(int, input().split(' '))
    c.append(_c)
    d.append(_d)

move = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        move[i][j] = abs(a[i] - c[j]) + abs(b[i] - d[j])

ans = [0] * n
for i in range(n):
    for j in range(m):
        _min = min(move[i])
        ans[i] = move[i].index(_min) + 1

for a in ans:
    print(a)