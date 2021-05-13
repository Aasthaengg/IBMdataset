from fractions import gcd
from functools import reduce

def lcm(a,b):
    return (a*b)//gcd(a,b)

def solve():
    N,M = map(int, input().split())
    S = input()
    T = input()
    gcd_NM = gcd(N,M)
    lcm_NM = (N*M)//gcd_NM
    S_diff = N // gcd_NM
    T_diff = M // gcd_NM
    
    i = 0
    possible = True
    while S_diff*i < N and T_diff*i < M:
        if S[S_diff*i] != T[T_diff*i]:
            possible = False
        i += 1
        
    print(lcm_NM if possible else -1)
    
solve()