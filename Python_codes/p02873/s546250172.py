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
    S = input()
    min_num = 0
    tmp_sum = 0
    diffs = deque()
    prev = ''
    ans = down = up = 0
    for i,c in enumerate(S):
        # dbg(i,ans)
        if c == '<':
            #trough
            if prev == '>':
                ans += down*(down-1)//2
                ans += max(down,up)
                down = up = 0
            ans += up
            up += 1
        
        else:
            down += 1

        prev = c

    #trough
    if S[-1] == '>':
        ans += down*(down-1)//2
        ans += max(down,up)
    if S[-1] == '<':
        ans += up

    print(ans)



    
main()