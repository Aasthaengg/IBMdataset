import bisect,collections,copy,heapq,itertools,math,string
import sys
def S(): return sys.stdin.readline().rstrip()
def M(): return map(int,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
pl = [I() for _ in range(N)]
pl.sort(reverse=True)
ans = 0
for i in range(N):
    if i == 0:
        ans += pl[i]//2
    else:
        ans += pl[i]
print(ans)