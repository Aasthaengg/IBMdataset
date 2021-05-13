N,K=map(int,input().split())
*A,=map(int,input().split())

i=0
L=0
R=0
while i<N:
    j=0
    while j<N:
        L+=(j<i and A[i]>A[j])
        R+=(i<j and A[i]>A[j])
        j+=1
    i+=1

ans=(R+L)*(K-1)*K//2+K*R
print(ans%(10**9+7))