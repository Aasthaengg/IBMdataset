n=int(input())
ans=0

if n==1:print(0);exit()


#12だったら[[2,2],[3,1]]みたいな、[素因数、次数]みたいに格納したい

import sys
import math
mod=10**9+7
inf=float("inf")
from math import sqrt
from collections import deque
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from functools import lru_cache
#メモ化再帰defの冒頭に毎回 @lru_cache(maxsize=10**10)
#引数にlistはだめ
#######ここまでテンプレ#######
#######ここから天ぷら########
from math import sqrt
def eratosu(n):
  if not isinstance(n,int):
    raise TypeError("nがint型になってねえぞ")
  if n<2:
    raise ValueError('nが2よりちっちぇえぞ')
  prime = []
  limit = sqrt(n)
  data = [i+1 for i in range(1, n)]  #2,3,4,...,n
  while True:
    p = data[0]
    if limit <= p:
        return prime + data
    prime.append(p)
    data = [e  for e in data if e % p != 0]
def bunkai(n):
    if n==2:
        return [[2,1]]
    if n==3:
        return [[3,1]]
    ans=[]
    temp=n
    #そんな早くしなくてよかったり、何回もするわけじゃないなら、
    #for i in range(2,int(sqrt(n))+1): とかで
    primelist=eratosu( int(sqrt(n)) )
    for i in primelist:
        if temp % i ==0:
            ji=0
            while temp%i==0:
                ji+=1
                temp//=i
            ans.append([i,ji])
    if ans==[]:return([[n,1]])  #素数のとき
    if temp!=1:
        ans.append([temp,1])  #4*5882353とか
    return ans

a=bunkai(n)

ans=0
import bisect as bi
p=[1,3,6,10,15,21,28,36,45,55]
for l in a:
  q=l[1]
  ans+=bi.bisect_right(p,q)
print(ans)
  
