from itertools import permutations
from math import sqrt

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
path = list(permutations(list(range(N))))

s = 0 #合計
for p in path:
    before = [lst[p[0]][0], lst[p[0]][1]]
    for i in range(1, N):
        s += sqrt((lst[p[i]][0] - before[0])**2 + (lst[p[i]][1] - before[1])**2)
        before[0] = lst[p[i]][0]
        before[1] = lst[p[i]][1]

#n!の計算
n = 1
for i in range(1, N+1):
    n *= i

print(s/n)