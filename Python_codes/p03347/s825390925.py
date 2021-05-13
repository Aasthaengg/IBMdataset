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
  n=I()
  l=[I() for _ in range(n)]

  if l[0]!=0:
    return -1

  ans=0
  st=l[0]
  for x in l[1:]:
    if st+1<x:
      return -1

    if x==st:
      ans+=x

    elif st<x:
      ans+=1

    elif st>x:
      ans+=x

    st=x

  return ans

# main()
print(main())
