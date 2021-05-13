N,P=map(int,input().split())
A=list(map(int,input().split()))
even=0
for i in range(N):
    if A[i]%2==0:
        even+=1

if even==N:
    if P==0:
        ans=2**N
    else:
        ans=0
else:
    ans=2**(N-1)

print(ans)