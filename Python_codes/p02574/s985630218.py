from functools import reduce
from math import gcd

n = int(input())
A = list(map(int, input().split()))
maxA = 10**6+5

def furui(x):
    memo = [0]*(x+1)
    for i in range(2, x+1):
        if memo[i]: continue
        memo[i] = i
        for j in range(i*i, x+1, i):
            if memo[j]: continue
            memo[j] = i
    return memo

memo = furui(maxA)
tf = [True]*(maxA)
for a in A:
    if a == 1: continue
    pfct = []
    while a > 1:
        pfct.append(memo[a])
        a //= memo[a]

    for b in set(pfct):
        if not tf[b]:
            break
        tf[b] = False
    else:
        continue
    break
else:
    print('pairwise coprime')
    exit()

if reduce(gcd, A) == 1:
    print('setwise coprime')
else:
    print('not coprime')