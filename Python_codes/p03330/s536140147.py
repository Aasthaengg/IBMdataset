import sys
import math
mod=10**9+7
inf=float("inf")
from math import sqrt
from collections import deque
from collections import Counter
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from functools import lru_cache
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#######ここから天ぷら########
n,c=map(int,input().split())
D=[]
for i in range(c):
    D.append(list(map(int,input().split())))
G=[]
for i in range(n):
    a=list(map(int,input().split()))
    G.append([i-1 for i in a])
A=[]
B=[]
C=[]
for i in range(n):
    for j in range(n):
        d=(i+j)%3
        if d==0:
            A.append(G[i][j])
        elif d==1:
            B.append(G[i][j])
        else:
            C.append(G[i][j])
A=Counter(A);B=Counter(B);C=Counter(C)
cost=inf
for s in range(c):
    for t in range(c):
        if s==t:continue
        for r in range(c):
            if s==r or t==r:continue
            cost=min(cost, sum(D[i][s]*j for i,j in A.items())+sum(D[i][t]*j for i,j in B.items())+sum(D[i][r]*j for i,j in C.items()))
print(cost)