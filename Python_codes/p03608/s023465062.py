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

n,m,r=map(int,input().split())
R=[i-1 for i in list(map(int,input().split()))]#いくまち
G=[[] for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1;b-=1
    G[a].append([c,b])
    G[b].append([c,a])  #G[i]:=iから出る道の[重み、行先]の配列


def dijkstra(s):
    dist=[inf for i in range(n)] #sからの距離のリスト
    dist[s]=0
    mirai=[True for i in range(n)] #Trueなら未確定
    mirai[s]=False

    queue=[] #こいつがheapqになる
    for kyori,to in G[s]:
        heapq.heappush(queue , kyori*10**6+to)  #重みと行先を1つの変数で表してる！
    while queue:
        minedge= heapq.heappop(queue)
        #miraiがTrueのやつ(未確定なやつ)から最小距離のものをさがす
        if not mirai[minedge%(10**6)]: continue
        #距離が小さいものから"確定"していく
        v=minedge%(10**6) #最小距離の頂点
        dist[v] = minedge//(10**6) #その距離
        mirai[v]=False
        for kyori,to in G[v]:
            if mirai[to]:
                heapq.heappush(queue, (kyori+dist[v])*(10**6)+to)
                #queueに入る数は、必ず「sからの」距離と行先を持っている
    return dist


from itertools import permutations as per
ans=inf
P=[dijkstra(i) for i in range(n)]
for l in per(R):
    now=0
    for i in range(r-1):
        now+=P[l[i]][l[i+1]]
    ans=min(ans,now)

print(ans)