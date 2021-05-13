from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
from decimal import Decimal
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m,K = inpl()
s = [input() for _ in range(n)]
res = INF
for pat in itertools.product([0,1], repeat=n-1):
    pat = list(pat) + [0]
    group = []
    tmp = []
    for i,j in enumerate(pat):
        tmp += [i]
        if j or i == n-1:
            group += [tmp]
            tmp = []
    
    ln = len(group)
    white = [[0]*ln for _ in range(m)]
    ccc = set()
    cnt = pat.count(1) 
    ok = True
    for i in range(m):
        for j,z in enumerate(group):
            for k in z:
                if s[k][i] == '1':
                    white[i][j] += 1
            if max(white[i]) > K:
                ok = False
                break
    if not ok: continue
    
    now = [0] * ln
    for i in range(m):
        ok = True
        for j in range(ln):
            if now[j] + white[i][j] > K:
                ok = False
                break
        if ok:
            for j in range(ln):
                now[j] += white[i][j]
        else:
            cnt += 1
            for j in range(ln):
                now[j] = white[i][j]
    res = min(res, cnt)
print(res)