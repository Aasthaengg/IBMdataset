N,K=map(int,input().split())
A=list(map(int,input().split()))
data=[0 for i in range(0,41)]
for i in range(0,N):
    for j in range(0,41):
        data[j]+=(A[i]>>j)&1
X=0
flag=1
for i in range(0,41):
    if flag==0:
        if N-data[40-i]>=data[40-i]:
            X+=2**(40-i)
    else:
        test=K>>(40-i) &1
        if test==1:
            if N-data[40-i]>=data[40-i]:
                X+=2**(40-i)
            else:
                flag=0

print(sum(X^A[i] for i in range(0,N)))
