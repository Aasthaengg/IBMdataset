import sys
import math
import heapq
mod=10**9+7
inf=float("inf")
from math import sqrt, ceil
from collections import deque, Counter, defaultdict, OrderedDict
#すべてのkeyが用意されてる defaultdict(int)で初期化
#順序を保ったdict
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########
n=int(input())
A=[]
# ans=0
for i in range(n):
    a=list(map(int,input().split()))
    A.append(a)
    # ans+=sum(a)

#ans//=2
miti=[[] for i in range(n)]
for i in range(n):
    miti[i]=A[i][:]
    
for k in range(n):
    for j in range(k):
        for i in range(j):
            q=A[i][j]
            w=A[j][k]
            e=A[k][i]
            #print(i,j,k,"\t",q,w,e)
            # q,w,e=sorted([[q,i,j],[w,j,k],[e,k,i]])
            # if max(q,w,e)==inf: continue
            if q+w==e and q!=inf and w!=inf: miti[k][i]=inf;miti[i][k]=inf;continue
            if q+w<A[k][i] and q!=inf and w!=inf: print(-1);exit()
            if w+e==q and e!=inf and w!=inf: miti[i][j]=inf;miti[j][i]=inf;continue
            if w+e<A[i][j]  and e!=inf and w!=inf : print(-1);exit()
            if e+q==A[j][k] and q!=inf and e!=inf: miti[j][k]=inf;miti[k][j]=inf;continue
            if e+q<A[j][k] and q!=inf and e!=inf: print(-1);exit()
            
            
                
            
ans=0
for i in range(n):
    for j in range(n):
        if miti[i][j]!=inf:
            ans+=miti[i][j]

print(ans//2)
