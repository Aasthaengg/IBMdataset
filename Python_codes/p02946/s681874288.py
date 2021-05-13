A=list(map(int,input().split()))
k=A[0]
x=A[1]
ans=[]
for i in range(x-k+1,k+x):
    ans.append(i)
print(*ans)