import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, M = MI()
A = LI()
ans = N - sum(A)
if ans >= 0:
    print(ans)
else:
    print(-1)