# 問題：https://atcoder.jp/contests/abc145/tasks/abc145_c

import math
import itertools

n = int(input())
x = []
y = []
for _ in range(n):
    X, Y = map(int, input().strip().split())
    x.append(X)
    y.append(Y)

distance = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        dist_i_j = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
        distance[i][j] = dist_i_j
        distance[j][i] = dist_i_j

p = itertools.permutations(range(n))
tmp_n = n
num_p = 1
while tmp_n > 1:
    num_p *= tmp_n
    tmp_n -= 1
res = 0
for perm in p:
    for i in range(n-1):
        dist = distance[perm[i]][perm[i+1]]
        res += dist / num_p

print(res)
