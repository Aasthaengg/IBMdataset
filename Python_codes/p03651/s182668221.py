import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    N,K=map(int,input().split())
    A=list(map(int,input().split()))

    ma=max(A)

    from functools import reduce
    from fractions import gcd

    g=reduce(gcd,A)
    if K%g==0 and K<=ma:
        print('POSSIBLE')
    else: print('IMPOSSIBLE')

resolve()