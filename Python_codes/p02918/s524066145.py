import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
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
  s=S()
  ans=0
  x=s[0]
  cnt=0
  for y in s[1:]:
    if x==y:
      cnt+=1
    else:
      ans+=cnt
      cnt=0
    x=y
  ans+=cnt

  ans=min(n-1,ans+2*k)

  return ans

# main()
print(main())
