from operator import mul
from functools import reduce

def combination(n, r):
    if not 0 <= r <= n: return 0
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

N = int(input())
S = input()

R = dict()
L = dict()


R["R"] = S.count("R")
L["R"] = 0
R["G"] = S.count("G")
L["G"] = 0
R["B"] = S.count("B")
L["B"] = 0

def num(n, x):
    res = 0
    for i in range(1,min(n,N-1-n) + 1):
        if S[n-i] != x and S[n+i] != x and S[n-i] != S[n+i]:
            res += 1
    return res

R[S[0]] -= 1
L[S[0]] += 1
res = 0
for i in range(1,N-1):
    x = S[i]
    R[x] -= 1
    three = sum( R[x]*L[x]for x in ["R","G","B"])
    res += three + ((N-1-i)-R[x])*L[x] + R[x]*(i-L[x]) + num(i,x)
    L[x] += 1

print(combination(N,3) - res)
