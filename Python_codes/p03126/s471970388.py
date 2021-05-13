import numpy as np
N,M = map(int,input().split())
A = [[int(i) for i in input().split()] for _ in range(N)]

ans=0
for i in range(1,M+1):
    count=0
    for j in range(N):
        if i in A[j][1:]:
            count+=1
        if count==N:
            ans+=1
print(ans)
