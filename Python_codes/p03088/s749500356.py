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
    N=I()
    D={
        "A":0, "G":1, "C":2, "T":3
    }

    DP=[[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N)] #DP[i][a][b][c] := i文字目までで、最後の文字ががabcな場合の数
    DP[1][3] = [[1]*4 for _ in range(4)] 
    for i in range(2,N):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for s in range(4):
                        if s==0: #なんでもOK
                            pass
                        elif s==1: #ACGだとout
                            if (b,c)==(D["A"],D["C"]):
                                continue
                        elif s==2: #AGC,GAC,A?GC,AG?Cがout
                            if (b,c) in ((D["A"],D["G"]), (D["G"],D["A"])) or (a,c) == (D["A"], D["G"]) or (a,b) == (D["A"], D["G"]) :
                                continue
                        else: #なんでもOK
                            pass
                        DP[i][b][c][s] += DP[i-1][a][b][c]
                        DP[i][b][c][s] %= mod

    ans = 0
    for a in DP[-1]:
        ans += sum([sum(i) for i in a])
    print(ans%mod)
    """
    AGC
    ACG
    GAC
    A?GC
    AG?C

    """
if __name__ == '__main__':
    main()
