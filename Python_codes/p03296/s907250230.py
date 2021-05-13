N=int(input())
A=[int(i) for i in input().split()]
check=10001
ans=0
for i in range(N-1):
    if A[i]==A[i+1]:
        A[i+1]=check
        ans+=1
print(ans)