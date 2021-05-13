N = int(input())
A = list(map(int,input().split()))
 
P=[0]*(N+1)
P[N]=A[N]
Q=[0]*(N+1)
Q[N]=A[N]
 
for i in range(N,0,-1):
    mxp=P[i]+A[i-1]
    mnp=(P[i]//2) + (P[i]%2) +A[i-1]
    mxq=Q[i]+A[i-1]
    mnq=(Q[i]//2) + (Q[i]%2) +A[i-1]
    P[i-1]=mnp
    Q[i-1]=min(mxq,2**i)
 
if P[0]!=1:
    print(-1)
    exit()
 
Q[0]=1
 
for i in range(1,N):
    if Q[i]>2**i:
        Q[i]=2**i
    if Q[i]>(Q[i-1]-A[i-1])*2:
        Q[i]=(Q[i-1]-A[i-1])*2
 
print(sum(Q))