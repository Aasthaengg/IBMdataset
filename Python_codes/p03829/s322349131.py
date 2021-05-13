N,A,B=map(int,input().split())
X=list(map(int,input().split()))
ans=0
for i in range(1,N):
    a=X[i]-X[i-1]
    b=a*A
    if b<B:
        ans+=b
    else:
        ans+=B
print(ans)