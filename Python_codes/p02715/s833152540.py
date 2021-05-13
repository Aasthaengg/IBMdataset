import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# n^p(mod m) -- START --
def powMod(n,p,m):
  if p==0:
    return 1
  if p%2==0:
    t=powMod(n,p//2,m)
    return t*t%m
  return n*powMod(n,p-1,m)%m
# n^p(mod m) --- END ---

def main():
  n,k=LI()
  ans=[0]*(k+1)
  for i in range(1,k+1)[::-1]:
    x=powMod((k//i),n,mod)
    for j in range(2,k//i+1):
      x-=ans[i*j]
    x%=mod
    ans[i]=x

  ret=0
  # print(ans)
  for i,x in enumerate(ans):
    ret+=x*i
    ret%=mod
  return ret

# main()
print(main())
