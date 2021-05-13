def main():
    from sys import setrecursionlimit, stdin, stderr
    from os import environ
    from collections import defaultdict, deque, Counter
    from math import ceil, floor
    from itertools import accumulate, combinations, combinations_with_replacement
    setrecursionlimit(10**6)
    dbg = (lambda *something: stderr.write("\033[92m{}\033[0m".format(str(something)+'\n'))) if 'TERM_PROGRAM' in environ else lambda *x: 0
    input = lambda: stdin.readline().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    P = 10**9+7
    INF = 10**18+10

    S = list(input())
    S = [1 if c == 'A' else 2 if c=='B' else 3 for c in S]
    N = len(S)
    ans = 0
    continuous_one = 0
    i = 0

    while i < N-1:
        if S[i] == 1:
            continuous_one += 1
            i += 1
        elif S[i] == 2 and S[i+1] == 3:
            ans += continuous_one
            i += 2
        else:
            continuous_one = 0
            i += 1
    

    



    print(ans)



    
main()