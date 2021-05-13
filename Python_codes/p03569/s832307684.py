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
  s=S()
  l=0
  r=len(s)-1

  ans=0
  while l<r:
    if s[l]=='x':
      if s[r]=='x':
        l+=1
        r-=1
      else:
        l+=1
        ans+=1
    else:
      if s[r]=='x':
        r-=1
        ans+=1
      else:
        if s[l]==s[r]:
          l+=1
          r-=1
        else:
          return -1

  return ans

# main()
print(main())
