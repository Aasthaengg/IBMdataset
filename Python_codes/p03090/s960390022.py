N=int(input())
ans=[]
if N%2==0:
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if i+j==N+1:
                continue
            ans.append([i,j])
else:
    for i in range(1,N):
        for j in range(i+1,N):
            if i+j==N:
                continue
            ans.append([i,j])
    for i in range(1,N):
        ans.append([i,N])
print(len(ans))
for u in ans:
    print(*u)