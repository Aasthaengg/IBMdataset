import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

# nCr
def nCr(n,r):
  return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

# 方針
# 大きい順から選ぶと平均は最大値を取れる
# 選んだ数字の最初と最後が違う場合、A個選んだ場合のみ平均が最大値になる
# よって最後の数の選び方が何通りあるかを求めればよい
# 最初と最後が同じ場合、選んだ数の種類は全て同じ
# よってその数を選ぶ方法は何通りあるかを求める

def main():
  n,a,b=LI()
  l=LI()

  l=sorted(l,key=lambda x:x,reverse=True)

  l2=l[:a]
  print(sum(l2)/len(l2))
  
  if l2[0]!=l2[-1]:
    c=l.count(l2[-1])
    c2=l2.count(l2[-1])
    print(nCr(c,c2))

  else:
    c=l.count(l2[-1])
    sm=0
    for i in range(a,min(b+1,c+1)):
      sm+=nCr(c,i)

    print(sm)

main()
