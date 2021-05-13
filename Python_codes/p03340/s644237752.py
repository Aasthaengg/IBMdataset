n=int(input())
A=list(map(int,input().split()))

B=[[] for i in range(n)]
for i in range(n):
    B[i]= [int(j) for j in  bin(A[i])[2:]]
    B[i]= [0]*(20-len(B[i]))+B[i]

ans=n
#累積和
R=[[] for i in range(n+1)]
R[0]=[0]*20
for i in range(n):
    R[i+1] = [l+k for l,k in zip(R[i], B[i])]
###

#転置
TR=[[0]*(n+1) for i in range(20)]
for i in range(n+1):
    for j in range(20):
        TR[j][i]=R[i][j]

from bisect import bisect_left as bi
for i in range(n,1,-1):
    now=R[i] ; #print(now)
    # score=
    ans+=i-max([bi(TR[k],now[k]-1) for k in range(20)])-1
    #print(ans)

print(ans)
