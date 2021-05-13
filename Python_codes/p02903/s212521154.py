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

def main():
  h,w,a,b=LI()
  field=[[0]*w for _ in range(h)]

  for i in range(b):
    for j in range(a):
      field[i][j]=1

  for i in range(b,h):
    for j in range(a,w):
      field[i][j]=1

  for x in field:
    print(''.join([str(y) for y in x]))

main()
# print(main())
