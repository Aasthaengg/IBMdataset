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
    S=list(ST())
    if S==list("abcdefghijklmnopqrstuvwxyz"):
        print("abcdefghijklmnopqrstuvwxz")
        return 
    exist = defaultdict(int)
    N=len(S)
    for s in S:
        exist[s]+=1
    if len(S)==26:
        flag = False
        for i in range(N)[::-1]:
            s = chr(ord("a")+i)
            if S[i]==s:
                flag = True
                continue
            if flag:
                exist_s = set(S[:i+1])
                for j in range(26):
                    t = chr(ord("a")+j)
                    if t not in exist_s and t>S[i]:
                        S[i]=t
                        break
            else:
                done = False
                for i in range(N-1)[::-1]:
                    if S[i]<S[i+1]:
                        for j in range(N)[::-1]:
                            if S[i]<S[j]:
                                S[i],S[j] = S[j],S[i]
                                # S[i+1:] = S[i+1:][::-1]
                                S=S[:i+1]
                                done = True
                                break
                    if done:
                        break
                if done:
                    print(*S,sep="")
                else:
                    print(-1)
                return
            break
        print(*S,sep="")
    else:
        for i in range(26):
            s = chr(i+ord("a"))
            if exist[s]==0:
                S+=s
                break
        print(*S,sep="")
        
if __name__ == '__main__':
    main()