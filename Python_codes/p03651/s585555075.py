from fractions import gcd
import functools

def gcd_list(l):
    return functools.reduce(gcd, l)

def solve():
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    d = gcd_list(A)
    ret = False
    if K > max(A):
        print('IMPOSSIBLE')
        return
    
    for a in A:
        if (a-K)%d == 0:
            ret = True
            break
            
    print('POSSIBLE' if ret else 'IMPOSSIBLE')
    
solve()