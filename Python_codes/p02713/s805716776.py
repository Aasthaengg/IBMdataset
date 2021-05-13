import functools
import math
def gcd_2(*vals):
    return functools.reduce(math.gcd, vals)
K = int(input())
ANS = 0
L = list(range(1, K+1))
M = list(range(1, K+1))
N = list(range(1, K+1))



for i in range(K):
    for j in range(K):
        for k in range(K):
            ANS = ANS + gcd_2(L[i], M[j], N[k])

print(ANS)