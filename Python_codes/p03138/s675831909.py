N,K=map(int,input().split())
A=list(map(int,input().split()))
data=[0 for i in range(0,41)]
for i in range(0,N):
    for j in range(0,41):
        data[j]+=(A[i]>>j)&1
X=0
subdata=[K>>i &1 for i in range(0,41)]
subdataK=[i for i in range(0,41) if subdata[i]==1]
ans=sum(K^A[i] for i in range(0,N))
for i in range(0,len(subdataK)):
    k=subdataK[i]#2^kの位で変化　2^0~2^k-1の位がフリー
    X=0
    for j in range(0,k):
        if N-data[j]>=data[j]:
            X+=2**j
    for j in range(k+1,41):
        X+=subdata[j]*2**j
    test=sum(X^A[i] for i in range(0,N))
    if test>ans:
        ans=test
print(ans)
