import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n,a,b=LI()
  l=LI()

  sm=0
  for i in range(n-1):
    x=l[i+1]-l[i]

    if x*a<b:
      sm+=x*a
    else:
      sm+=b

  return sm

print(main())
