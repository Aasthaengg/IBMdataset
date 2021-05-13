n=int(input())
ans=[]
for i in range(1,n+1):
    for j in range(i+1,n+1):
        ans.append((i,j))

if n%2:
    for i in range(1,n//2+1):
        ans.remove((i,n-i))
else:
    for i in range(1,n//2+1):
        ans.remove((i,n-i+1))

print(len(ans))
for x,y in ans:
    print(x,y)
