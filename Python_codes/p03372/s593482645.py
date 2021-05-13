#
# 　　  ⋀_⋀　 
#　　  (･ω･)  
# .／ Ｕ ∽ Ｕ＼
#  │＊　合　＊│
#  │＊　格　＊│ 
#  │＊　祈　＊│ 
#  │＊　願　＊│ 
#  │＊　　　＊│ 
#      ￣
#
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
from math import floor,sqrt,factorial,hypot,log #log2ないｙｐ
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from copy import deepcopy
from fractions import gcd
from random import randint
def ceil(a,b): return (a+b-1)//b
inf=float('inf')
mod = 10**9+7
def pprint(*A): 
    for a in A:     print(*a,sep='\n')
def INT_(n): return int(n)-1
def MI(): return map(int,input().split())
def MF(): return map(float, input().split())
def MI_(): return map(INT_,input().split())
def LI(): return list(MI())
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return list(MF())
def LIN(n:int): return [I() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]
def LLIN_(n: int): return [LI_() for _ in range(n)]
def LLI(): return [list(map(int, l.split() )) for l in input()]
def I(): return int(input())
def F(): return float(input())
def ST(): return input().replace('\n', '')
def main():
    N,C=MI()
    XV=LLIN(N)
    DP1 = [0]*(N+1)
    DP2 = [0]*(N+1)
    before = 0
    for i,(x,v) in enumerate(XV):
        DP1[i+1]=DP1[i]+v-(abs(x-before))
        before = x
    before = C
    for i,(x,v) in enumerate(XV[::-1]):
        DP2[i+1]=DP2[i]+v-(abs(x-before))
        before = x
    ans = max(max(DP1),max(DP2))
    now = 0

    DP1_ = [d-XV[i][0] for i,d in enumerate(DP1[1:])]
    DP2_ = [d-(C-XV[~i][0]) for i,d in enumerate(DP2[1:])]
    for i in range(N-1):
        if(DP2_[i+1]<DP2_[i]):
            DP2_[i+1] = DP2_[i]
        if(DP1_[i+1]<DP1_[i]):
            DP1_[i+1] = DP1_[i]
    now1 = 0
    now2 = 0
    for i in range(N):
        idx = N-1-i
        # print(DP1[i],DP2_[idx])
        # print(DP2[i],DP1_[idx])
        ans = max(ans,DP1[i]+DP2_[idx])
        ans = max(ans,DP2[idx]+DP1_[i])
        # print(ans)
    # print(DP1)
    # print(DP2)
    # print(DP1_)
    # print(DP2_)
    print(ans)

if __name__ == '__main__':
    main()
