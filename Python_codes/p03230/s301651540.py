from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
for i in range(1,10**5):
    tmp = i*(i+1)//2
    if n == tmp:
        k = i+1
        break
    elif n < tmp:
        print('No'); quit()
res = [[0 for j in range(k-1)]for i in range(k)]
cnt = 1
for i in range(k):
    for j in range(k-1-i):
        res[i][j] = cnt
        cnt += 1
# print(res)
cnt = 1
for j in range(k-1)[::-1]:
    for i in range(k):
        if res[i][j]: continue
        res[i][j] = cnt
        cnt += 1

print('Yes')
print(k)
for i in range(k):
    print(k-1,*res[i])
