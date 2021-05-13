A=list(map(int,input().split()))
ans=A[1]
for i in range(0,A[0]-1):
    ans=ans*(A[1]-1)
print(ans)
