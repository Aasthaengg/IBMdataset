import sys
mod=10**9+7 ; inf=float("inf")
from math import sqrt, ceil
from collections import deque, Counter, defaultdict #すべてのkeyが用意されてる defaultdict(int)で初期化
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
from bisect import bisect_left as bileft, bisect_right as biright
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########
n,m=map(int,input().split()) 
G=[] ; Y=[]
G1=[[] for i in range(n)]
for i in range(m):
    a,b,w=map(int,input().split())
    a-=1;b-=1
    G.append([a,b,-w])

# den=set([])
# for i  in range(m):
#     if uf.same(0,Y[i][0]): 
#         G.append(Y[i])
#         den.add(Y[i][0]);den.add(Y[i][1])
# now=len(den)

if 1:
    ansdist=[inf for i in range(n)]
    ansdist[0]=0
    for i in range(n-1):
        for edge in G:
            a,b,d=edge
            #辺ごとに見ていき、infでない(到達済み)頂点から伸びた辺であり、最小値を更新できるようなら緩和する
            if ansdist[b] > ansdist[a]+d:  #inf>inf はFalse
                ansdist[b]= ansdist[a]+d
                # if i==2*n+2 : print("inf");exit()

    # return ansdist

ans=-ansdist[-1]
neg=[0]*n
for i in range(n):
    for edge in G:
        a,b,d=edge
        if ansdist[b]>ansdist[a]+d:
            ansdist[b] = ansdist[a]+d
            neg[b]=1
        if neg[a]:neg[b]=1
if neg[-1]:
    print("inf")
else:
    print(ans)

