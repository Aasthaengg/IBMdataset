n=int(input())
A=[list(map(int,input().split())) for _ in range(2)]
ans=0
for i in range(n):
    m=0
    m+=sum(A[0][0:i+1])+sum(A[1][i:n+1])
    ans=max(ans,m)
print(ans)