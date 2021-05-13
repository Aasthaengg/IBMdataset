import bisect,collections,copy,heapq,itertools,math,numpy,string,decimal
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
K = I()
x = LI()

ans = 0

for xi in x:
  ans += min(xi,abs(K-xi))
print(ans*2)