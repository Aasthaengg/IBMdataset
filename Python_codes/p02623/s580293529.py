N,M,K=map(int,input().split())
*A,=map(int,input().split())
*B,=map(int,input().split())

AX=[0]*(N+1)
na=N+1
for i in range(1,N+1):
    AX[i]=AX[i-1]+A[i-1]
    if K<AX[i]:na=min(na,i)

BX=[0]*(M+1)
nb=M+1
for i in range(1,M+1):
    BX[i]=BX[i-1]+B[i-1]
    if K<BX[i]:nb=min(nb,i)

import bisect        
ans=0
for i in range(na):
 j=bisect.bisect_right(BX,K-AX[i])-1
 # print(na,t,i,j)
 ans=max(ans,i+j)
            
print(ans)