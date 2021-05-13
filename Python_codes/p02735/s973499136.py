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

    H,W = LMIIS()
    table = [0]*H
    for i in range(H):
        table[i] = input()
    num_route = [[0]*W for _ in range(H)]

    if table[0][0] == '#':
        num_route[0][0] = 1

    for i in range(1,W):
        if table[0][i] == '#' and table[0][i] != table[0][i-1]:
            num_route[0][i] = num_route[0][i-1] + 1
        else:
            num_route[0][i] = num_route[0][i-1]

    for i in range(1,H):
        if table[i][0] == '#' and table[i][0] != table[i-1][0]:
            num_route[i][0] = num_route[i-1][0] + 1
        else:
            num_route[i][0] = num_route[i-1][0]
    
    for i in range(1,H):
        for j in range(1,W):
            l = u = 0
            if table[i][j] == '#' and table[i][j] != table[i][j-1]:
                l = num_route[i][j-1] + 1
            else:
                l = num_route[i][j-1]
            if table[i][j] == '#' and table[i][j] != table[i-1][j]:
                u = num_route[i-1][j] + 1
            else:
                u = num_route[i-1][j]
            num_route[i][j] = min(l,u)
            
    #print(num_route)
    print(num_route[H-1][W-1])

if __name__ == '__main__':
    main()