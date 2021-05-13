n,d=map(int,input().split())
l=(list(input().split() for _ in range(n)))
ans=0
for i in range(n):
    b=int(l[i][0])
    c=int(l[i][1])
    a=(b**2)+(c**2)
    if a <= d**2:
        ans+=1
print(ans)
