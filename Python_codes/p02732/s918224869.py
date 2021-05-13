from operator import mul
from functools import reduce

def cmb(n,r):
    if n < r:
        return 0
    else:
        r = min(n-r,r)
        if r == 0: return 1
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1,r + 1))
        return over // under

N = int(input())
A = list(map(int,input().split()))

num_dict = {i:0 for i in range(1,N+1)}
for i in range(N):
    num_dict[A[i]] += 1

S = 0
for i in range(1,N+1):
    S += cmb(num_dict[i],2)

for i in range(N):
    tmp = 0
    S_dif = cmb(num_dict[A[i]]-1,2) - cmb(num_dict[A[i]],2)
    tmp = S + S_dif
    print(tmp)