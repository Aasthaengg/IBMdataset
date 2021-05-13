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
    tmp = 0
    S = list(input())
    N = len(S)+1
    A = [0]*N
    num_conti = 0
    for i in range(N-1):
        if S[i] == '<':
            num_conti += 1
        else:
            num_conti = 0
        A[i+1] = num_conti
    num_conti = 0
    for i in range(N-2,-1,-1):
        if S[i] == '>':
            num_conti += 1
        else:
            num_conti = 0
        A[i] = max(A[i],num_conti)
    print(sum(A))
    dbg(A)





    
main()