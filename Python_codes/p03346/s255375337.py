n=int(input())
d={}
for i in range(n):
    p=int(input())
    d[p]=i+1
ans=s=1
while s<n:
    f=d[s]
    cnt=0
    for i in range(s,n+1):
        if d[i]>=f:
            f=d[i]
            s=i
            cnt+=1
        else:
            s=i
            break
    ans=max(ans,cnt)
print(n-ans)