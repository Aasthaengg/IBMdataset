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
    N,M = map(int,input().split())
    count_list = [0]*(N+1)
    for _ in range(M):
        a,b = map(int,input().split())
        count_list[a] += 1
        count_list[b] += 1
    for c in count_list:
        if c% 2 == 1:
            print('NO')
            return
    print('YES')
    return

    

if __name__ == '__main__':
    main()