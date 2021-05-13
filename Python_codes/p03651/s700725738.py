import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    n,k=map(int,input().split())
    A=list(map(int,input().split()))

    from functools import reduce
    from fractions import gcd
    G=reduce(gcd,A)

    if k%G==0 and k<=max(A):
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

resolve()
