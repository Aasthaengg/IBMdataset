
N,K = map(int,input().split())

import sys
if K > ((N-1)*(N-2)//2):
    print(-1)
    sys.exit()
    
edge = []
for i in range(N-1):
    edge.append([i+1,N])

nums = (N-1)*(N-2)//2 - K
for i in range(N-1):
    for j in range(i+1,N-1):
        if nums==0:break
        edge.append([i+1,j+1])
        nums-=1
    if nums==0:break

print(len(edge))
for u,v in edge:
    print(u,v)
