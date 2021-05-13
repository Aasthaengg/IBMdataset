N,K,Q=map(int,input().split())
A=[int(input()) for _ in range(Q)]
L=[K-Q]*N
for i in range(Q):
    L[A[i]-1]+=1
for j in range(N):
    if  L[j]<=0:
        print('No')
    else:
        print('Yes')