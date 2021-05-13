from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

M,K = inpl()
MAX = 2**M

if M != 1 and MAX > K:
    ans = []
    for i in range(MAX):
        if i != K:
            ans.append(i)
    ans.append(K)
    for i in reversed(range(MAX)):
        if i != K:
            ans.append(i)
    ans.append(K)
    print(' '.join(map(str,ans)))
elif M == 1:
    if K == 0:
        print('0 0 1 1')
    else:
        print(-1)
else:
    print(-1)
