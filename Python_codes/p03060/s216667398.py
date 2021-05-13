import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
Vl = LI()
Cl = LI()
ans = 0
for i in range(N):
    if Vl[i] - Cl[i] > 0:
        ans += Vl[i] - Cl[i]
print(ans)