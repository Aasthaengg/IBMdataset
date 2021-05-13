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
    A = LMIIS()
    B = LMIIS()
    GA = deque() #ai > bi の組
    GB = deque()
    for a,b in zip(A,B):
        if a > b:
            GA.append(a-b)
        elif a < b:
            GB.append(b-a)
    
    for ga in GA:
        tmp = ga
        while GB:
            gb = GB.popleft()
            if gb >= tmp*2:
                GB.append(gb-tmp*2)
                break
            else:
                tmp -= gb//2
        if len(GB) == 0:
            print('No')
            return
    print('Yes')
        
    

if __name__ == '__main__':
    main()