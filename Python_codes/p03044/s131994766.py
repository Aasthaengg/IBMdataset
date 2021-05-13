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

color=[-1]*100100
G=[[] for _ in range(100100)]

def f(st):
  st_c=color[st]
  for v,d in G[st]:
    if color[v]!=-1:
      continue

    if d%2==0:
      color[v]=st_c
    else:
      color[v]=abs(st_c-1)

    f(v)

def main():
  n=I()
  for _ in range(n-1):
    a,b,c=LI()
    a-=1
    b-=1
    G[a].append((b,c))
    G[b].append((a,c))

  color[0]=0
  f(0)

  for i in range(n):
    print(color[i])

main()
# print(main())
