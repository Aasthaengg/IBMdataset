N,M=map(int,input().split())
A=list(map(int,input().split()))
k=0
l=0
for i in range(N):
    k+=A[i]
for i in range(N):
    if ((A[i]/k)>=(1/(4*M))):
        l+=1
if l>=M:
    print('Yes')
else:
    print('No')