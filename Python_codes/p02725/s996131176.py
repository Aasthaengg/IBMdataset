n,k=map(int,input().split())
A=list(map(int,input().split()))
S=[0 for _ in range(k)]

for i in range(1,k+1):
    if i!=k:
        S[i-1]=A[i]-A[i-1]
    else:
        S[i-1]=A[0]+n-A[k-1]

print(n-max(S))
