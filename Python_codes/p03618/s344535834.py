from operator import mul
from functools import reduce


A = input()
N = len(A)
ans = N*(N-1)//2

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

for i in range(26):
    num = A.count(chr(ord('a') + i))
    
    if num >= 2:
        ans -= cmb(num,2)

print(ans+1)