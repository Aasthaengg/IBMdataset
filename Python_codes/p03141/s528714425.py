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
    S = []
    for i in range(N):
        a,b = LMIIS()
        S.append((a+b,a,b))
    S.sort(reverse=True)
    # print(S)
    ans = 0
    for i, item in enumerate(S):
        sumab,a,b = item
        if i % 2 == 0:
            ans += a
        else:
            ans -= b
    print(ans)

if __name__ == '__main__':
    main()