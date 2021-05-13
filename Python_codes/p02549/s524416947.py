import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=998244353
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n,k=LI()
  field=[LI() for _ in range(k)]

  dp=[0]*(n+1)
  dpsum=[0]*(n+1)
  dp[1]=1
  dpsum[1]=1

  for i in range(2,n+1):
    for l,r in field:
      li=i-r
      ri=i-l
      if ri<=0:
        continue
      li=max(1,li)
      dp[i]+=dpsum[ri]-dpsum[li-1]
      dp[i]%=mod
    dpsum[i]=dp[i]+dpsum[i-1]
    dpsum[i]%=mod
  
  return dp[n]%mod

# main()
print(main())
