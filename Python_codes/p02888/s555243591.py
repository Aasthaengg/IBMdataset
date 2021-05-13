from itertools import combinations
from bisect import *
def max2(x,y):
    return x if x > y else y
N = int(input())
L = list(map(int, input().split()))
L.sort()
res = 0
for i, j in combinations(range(N), 2):
    a, b = L[i], L[j]
    res += max2(bisect_left(L, a+b) -1 - j, 0)
print(res)