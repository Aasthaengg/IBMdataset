N=int(input())
K=int(input())
X=list(map(int,input().split()))

D=0
for i in range(N):
    d=min(X[i],K-X[i])
    D+=d
print(2*D)
