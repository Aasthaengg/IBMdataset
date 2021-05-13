n=int(input())
A=list(map(int,input().split()))
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

C=Counter(A)
NUM=[]
if n%3!=0:
    if len(C)!=1 or A[0]!=0:
        print("No");exit()
    else:
        print("Yes");exit()
if all([i%(n//3)==0 for i in C.values()]):
    for i,v in C.items():
        if v==n//3:
            NUM.append(i)
        if v==n*2//3:
            NUM.append(i)
            NUM.append(i)
        if v==n:
            if i==0:print("Yes");exit()
            print("No");exit()
    a,b,c=NUM
    print("Yes" if a^b==c else "No");exit()
print("No")