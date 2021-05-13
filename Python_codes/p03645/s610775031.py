n,m=map(int,input().split())
A=[0]*n
B=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    if a==1:
        A[b-1]=1
    if b==n:
        B[a-1]=1

ans="IMPOSSIBLE"
for i in range(n):
    if A[i]==1 and B[i]==1:
        ans="POSSIBLE"
        break
print(ans)