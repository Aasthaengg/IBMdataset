from math import gcd
from functools import reduce
k=10**6+1
def judge(n,a):
  c=[0]*k
  for x in a:
    c[x]+=1 #対応する数の個数を記録
  t=any(sum(c[i::i])>1 for i in range(2,k)) #自身を約数に持つ数が2つ以上与えられたリストに存在するような数が一つでもあるかどうか
  t+=reduce(gcd,a)>1 #全体について1以外の公約数があれば1加える
  return ['pairwise','setwise','not'][t]+' coprime' #全体に公約数があればt=2,全体の公約数が1で公約数持つペアがあればt=1
n=int(input())
a=list(map(int,input().split()))
print(judge(n,a))
