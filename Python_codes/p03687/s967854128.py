s=input()
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

# C=Counter(s)
n=len(s)
ans=n+1
for c in range(ord("a"),ord("z")+1):
    c=chr(c)
    now=[]
    for v,cc in enumerate(s):
        if cc==c:
            now.append(v)
    if len(now)==0: continue
    #print(n,c,now)
    d=[now[0]]
    d+=[ (now[i+1]-now[i]-1) for i in range(len(now)-1) ]+[n-1-now[-1]]
    ans=min( max(d),  ans )
print(ans)