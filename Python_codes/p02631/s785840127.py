n=int(input())
a=list(map(int,input().split()))
total=a[0]
for i in range(1,n):
    total^=a[i]
ans=[]
for i in range(n):
    ans.append(total^a[i])
print(*ans)