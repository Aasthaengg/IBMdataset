from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())

aa = list(input())
N = len(aa)
cnt = [0]*26

for a in aa:
    cnt[ord(a)-97] += 1

ans = N*(N-1)//2+1
for n in cnt:
    ans -= n*(n-1)//2

print(ans)
