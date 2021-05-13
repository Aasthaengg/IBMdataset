from collections import deque
from copy import deepcopy
import heapq

N,K=list(map(int,input().split()))
V=list(map(int,input().split()))

minus=[[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

vdeque=deque(V)

for left in range(N+1):
    for right in range(N-left+1):
        v=deepcopy(vdeque)
        q=[]

        tleft=left
        while tleft>0:
            vi=deque.popleft(v)
            if vi<0:
                heapq.heappush(q,vi)
            tleft-=1
        
        tright=right

        while tright>0:
            vj=deque.pop(v)
            if vj<0:
                heapq.heappush(q,vj)
            tright-=1
        
        for k in range(1,N+1):
            if len(q)>0:
                minus[k][left][right]=minus[k-1][left][right]-heapq.heappop(q)
            else:
                minus[k][left][right]=minus[k-1][left][right]

leftacum=[0]*(N+1)
rightacum=[0]*(N+1)

for i in range(N):
    leftacum[i+1]=leftacum[i]+V[i]
    rightacum[i+1]=rightacum[i]+V[N-i-1]

ans=-10**10

for left in range(N+1):
    for right in range(N-left+1):
        k=min(N,K-left-right)
        if k<0:
            continue

        ans=max(ans,leftacum[left]+rightacum[right]+minus[k][left][right])

print(ans)