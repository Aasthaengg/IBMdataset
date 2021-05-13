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

    S = II()
    if S == 10**18:
        x1,y1,x2,y2,x3,y3 = 0,0,10**9,0,0,10**9
    else:
        x1,y1,x2,y2 = 0,0,10**9,1
        y3 = 0 if S < 10 ** 9 else S // 10**9 + 1
        x3 = S % 10**9 if y3 == 0 else 10**9 - S % 10 ** 9
    print(x1,y1,x2,y2,x3,y3)
    assert(abs(x3*y2-y3*x2)==S)
    assert(x3 <= 10**9)
    assert(y3 <= 10**9)



if __name__ == '__main__':
    main()