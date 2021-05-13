from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())

K = int(input())
aa = reversed(inpl())

MIN = MAX = 2
for a in aa:
    if MIN%a == 0 or MAX//a - MIN//a > 0:
        MIN = ((MIN-1)//a+1) *a
        MAX = MAX//a*a+a-1
    else:
        print(-1)
        sys.exit()

print(MIN,MAX)
