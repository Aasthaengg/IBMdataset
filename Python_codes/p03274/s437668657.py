def main():
    from sys import setrecursionlimit, stdin
    from os import environ
    from collections import defaultdict, deque, Counter
    # from math import ceil, floor, gcd
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7

    N,K = LMIIS()
    X = LMIIS()


    #left:X[0] right:X[K-1]
    left = 0
    right = K-1
    syaku = X[right] - X[left]
    if abs(X[left]) > abs(X[right]):
        min_time = syaku + abs(X[right])
    else:
        min_time = syaku + abs(X[left])


    for i in range(N-K+1):
        syaku = X[right] - X[left]
        if abs(X[left]) > abs(X[right]):
            min_time = min(min_time, syaku + abs(X[right]))
        else:
            min_time = min(min_time, syaku + abs(X[left]))
        
        left += 1
        right += 1
    
    print(min_time)



    
main()