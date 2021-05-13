s=input();n=len(s)
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

# @lru_cache(maxsize=10**10)
def qq(i):
    if i==1:
        if s[0]==s[1]: return 1
        return 2
    if i==2:
        if s[0]!=s[1] and s[1]!=s[2]: return 3
        return 2
    if i==0:
        return 1
    if s[i]==s[i-1]:
        return qq(i-3)+2
    else:
        return qq(i-1)+1
print(qq(n-1))