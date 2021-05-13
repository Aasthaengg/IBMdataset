N,A,B=map(int,input().split())
X=list(map(int,input().split()))
Y=[0 for k in range(N-1)]
for k in range(N-1):
    Y[k]=X[k+1]-X[k]
ans=0
for k in range(N-1):
    ans+=min(A*Y[k],B)
print(ans)
