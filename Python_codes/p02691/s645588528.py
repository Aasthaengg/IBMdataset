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

def main():
  n=I()
  l=LI()

  # j-i=Ai+Aj
  # Ai+i=j-Aj

  a=[]
  b={}
  for i in range(n):
    x=l[i]
    a.append(x+i)
    y=i-x
    if y in b:
      b[y]+=1
    else:
      b[y]=1

  ans=0
  for x in a:
    if x in b:
      ans+=b[x]

  return ans

# main()
print(main())
