import sys
from itertools import accumulate
N, C = [int(i) for i in sys.stdin.readline().split()]
ls = {j : [0 for i in range(2*10**5)] for j in range(1,C+1)}
for i in range(N):
    s, t, c = [int(i) for i in sys.stdin.readline().split()]
    ls[c][s] += 1
    ls[c][t+1] -= 1

res = [0 for i in range(2*10**5)]
for _c in range(1, C+1):
    for i, j in enumerate(accumulate(ls[_c])):
        res[i] += min(1,j)
print(max(res))