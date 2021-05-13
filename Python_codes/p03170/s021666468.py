N,K=map(int,input().split())
A=sorted(map(int,input().split()))
d=[0]*(K+1)
for i in range(K):
    x=d[i]^1
    if x:
        for a in A:
            if i+a<K+1:
                d[i+a]=x
print(['Second','First'][d[-1]])