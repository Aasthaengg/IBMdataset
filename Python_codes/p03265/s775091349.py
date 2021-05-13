import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

x1,y1,x2,y2 = II()


x3=x2+(y1-y2)
y3=y2-(x1-x2)
x4=x1+(y1-y2)
y4=y1-(x1-x2)

print(x3,y3,x4,y4)