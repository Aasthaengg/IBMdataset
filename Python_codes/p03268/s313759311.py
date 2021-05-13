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
    N,K = LMIIS()
    ans = 0

    if K % 2 == 1:
        print((N//K)**3)
        return
    
    
    

    #(N//K) ありうるKの倍数の数(0以外)

    #a,b,c,全部がKの倍数 のパターン
    ans += (N//K)**3
    #a,b,c,全部がKの倍数+K//2　のパターン
    ans += ((N-K//2)//K+1)**3
    print(ans)


    


    





    
main()