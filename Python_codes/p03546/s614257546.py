def main():
    from sys import setrecursionlimit, stdin
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**9+10

    H,W = LMIIS()
    C = []
    for i in range(10):
        C.append(LMIIS())
    A = []
    for i in range(H):
        A.append(LMIIS())
    
    from copy import deepcopy
    for m in range(10):
        for f in range(10):
            for t in range(10):
                C[f][t] = min(C[f][t], C[f][m] + C[m][t])


    
    ans = 0
    for line in A:
        for a in line:
            if abs(a) != 1:
                ans += C[a][1]
    print(ans)


    
main()