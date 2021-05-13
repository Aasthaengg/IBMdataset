n=int(input())
ans=[]
if n%2:
    for i in range(1,n):
        ans.append((i,n))
    for i in range(1,n):
        for j in range(i+1,n):
            if j!=n-i:
                ans.append((i,j))
else:
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if j!=n+1-i:
                ans.append((i,j))
print(len(ans))
for a in ans:
    print(*a)