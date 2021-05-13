#coding:utf-8
import sys,os
from collections import defaultdict, deque
from fractions import gcd
from math import ceil, floor
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    XLMIIS = lambda x: [LMIIS() for _ in range(x)]
    YN = lambda c : print('Yes') if c else print('No')
    MOD = 10**9+7

    N = II()
    g = {'Vacant':0, 'Male':1, 'Female':2}



    print(0,flush=True)
    sl = g[input()]
    if sl == 0:
        return

    print(N-1,flush=True)
    sr = g[input()]
    if sr == 0:
        return
    
    l = 0
    r = N-1
    while r-l>1:

        m = (l+r)//2
        print(m,flush=True)
        a = g[input()]
        if a == 0:
            return
        
        if (m-l) % 2 == 1:
            if sl == a:
                r = m
                sr = a
            else:
                l = m
                sl = a

        else:
            if a != sl:
                r = m
                sr = a
            else:
                l = m
                sl = a
        

    print(-1)


if __name__ == '__main__':
    main()