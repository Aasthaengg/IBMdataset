import sys
input=sys.stdin.readline

import heapq as hq

x,y,z,k=map(int,input().split())
A=list(reversed(sorted(map(int,input().split()))))
B=list(reversed(sorted(map(int,input().split()))))
C=list(reversed(sorted(map(int,input().split()))))
P=[]
hq.heapify(P)
for a in A:
    for b in B:
        hq.heappush(P,-(a+b))
Q=[]
hq.heapify(Q)
for i in range(min(x*y,3000)):
    p=-hq.heappop(P)
    for c in C:
        hq.heappush(Q,-(p+c))
for i in range(k):
    print(-hq.heappop(Q))