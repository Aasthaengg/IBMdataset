N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=list(map(int, input().split()))

ans=B[A[0]-1]
for i in range(1,N):
    j=A[i-1]-1
    k=A[i]-1
    ans+=B[k]
    if j+1==k:
      ans+=C[j]
print(ans)