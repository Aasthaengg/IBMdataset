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

    
    H,W,A,B = LMIIS()
    l1 = '0'*A + '1'*(W-A)
    l2 = '1'*A + '0'*(W-A)
    for i in range(B):
        print(l1)
    for i in range(H-B):
        print(l2)
        

if __name__ == '__main__':
    main()