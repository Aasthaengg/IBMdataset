def main():
    from sys import setrecursionlimit, stdin
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor, gcd
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**9+10
    U = list()
    L = list()
    N = II()
    for i in range(N):
        a,b = LMIIS()
        U.append(b)
        L.append(a)
    U.sort()
    L.sort()
    if N % 2 == 1:
        upper = U[(1+N)//2-1]
        lower = L[(1+N)//2-1]
        print(int(upper-lower)+1)
    else:
        upper = (U[N//2-1]+U[N//2])
        lower = (L[N//2-1]+L[N//2])
        print(upper-lower+1)
    
    
        




    
main()