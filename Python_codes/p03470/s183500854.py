n=int(input())
d=[int(input()) for _ in range(n)]
d.sort()
ans=1
for i in range(n-1):
    if d[i]<d[i+1]:
        ans+=1
print(ans)