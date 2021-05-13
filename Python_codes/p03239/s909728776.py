import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
N, T = M()
ans = 100000
for _ in range(N):
    c, t = M()
    if t <= T:
        ans = min(ans, c)
if ans == 100000:
    print('TLE')
else:
    print(ans)