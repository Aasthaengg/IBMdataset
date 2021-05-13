h,w=map(int,input().split())
A=[list(input()) for i in range(h)]
import sys
mod=10**9+7 ; inf=float("inf")
from math import sqrt, ceil
from collections import deque, Counter, defaultdict #すべてのkeyが用意されてる defaultdict(int)で初期化
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal as D  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
from bisect import bisect_left as bileft, bisect_right as biright
from fractions import Fraction as F  #F(a,b)で正確なa/b
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########

queue=deque([])
seen=[[0]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        if A[i][j]=="#":
            queue.append([i,j,0])
            seen[i][j]=1

dx=[1,0,-1,0];dy=[0,1,0,-1]
while queue:
    x,y,t=queue.pop()
    for i,j in zip(dx,dy):
        if 0<=x+i<h and 0<=y+j<w and seen[x+i][y+j]==0:
            queue.appendleft([x+i,y+j,t+1])
            seen[x+i][y+j]=1
print(t)
