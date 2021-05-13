import sys
input = sys.stdin.readline
from bisect import *
from heapq import *

N, D, A = map(int, input().split())
XH = [tuple(map(int, input().split())) for _ in range(N)]
XH.sort(key=lambda k: k[0])
pq = []
ans = 0
S = 0

for i in range(N):
    X, H = XH[i]
    
    while len(pq)>0:
        if pq[0][0]<X:
            t = heappop(pq)
            S -= t[1]
        else:
            break
        
    H -= S
    
    if H<=0:
        continue
    
    cnt = (H+A-1)//A
    ans += cnt
    heappush(pq, (X+2*D, cnt*A))
    S += cnt*A

print(ans)