n=int(input())
A=list(map(int,input().split()))
ans=set()
for i in range(1,n):A[i]+=A[i-1]
for i in range(n-1):
    ans.add(abs(A[-1]-A[i]-A[i]))
print(min(ans))