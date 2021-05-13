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

  l=0
  r=n-1

  print(0)
  _ans=S()
  if _ans=='Vacant':
    return
  l_ans=_ans

  print(n-1)
  _ans=S()
  if _ans=='Vacant':
    return
  r_ans=_ans

  while True:
    x=(l+r)//2
    print(x)

    ans=S()
    if ans=='Vacant':
      return

    if (x-l)%2==0:
      if l_ans==ans:
        l=x
      else:
        r=x
    else:
      if l_ans!=ans:
        l=x
        l_ans=ans
      else:
        r=x
        r_ans=ans

main()
# print(main())
