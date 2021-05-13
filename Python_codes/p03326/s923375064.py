N,M=map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
import copy
import heapq
ans=0

for i in range(8):
    li=[]
    heapq.heapify(li)
    hoge=[1,1,1]

    for j in range(3):
        if ((i >> j) & 1):
            hoge[j]=-1
    for k in range(N):
        tmp=0
        for r in range(3):
            tmp += S[k][r] * hoge[r]
        heapq.heappush(li, tmp)
    re=0
    for t in range(M):
        re += heapq.heappop(li)

    re = abs(re)
    if re > ans :
        ans=re

print(ans)