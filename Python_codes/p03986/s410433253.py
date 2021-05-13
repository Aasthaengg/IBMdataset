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

    S = input()
    num_s = 0
    ans = len(S)
    for c in S:
        if c == 'S':
            num_s += 1
        else:
            if num_s > 0:
                num_s -= 1
                ans -= 2
    print(ans)

    
main()