import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# 1点を0,0で固定、面積公式よりx1y2-x2y1=S
# x1=10**9,x2=1(0にすると変数が減るので駄目？)
# y2を切り上げ気味に近づける（切り下げ気味だとy1が負になりうる）
# x2y1=x1y2-Sよりy1も求まる

def main():
  s=I()
  x1=0
  y1=0
  x2=10**9
  x3=1
  y3=(s+x2-1)//x2
  y2=x2*y3-s

  print(x1,y1,x2,y2,x3,y3)

main()
# print(main())
