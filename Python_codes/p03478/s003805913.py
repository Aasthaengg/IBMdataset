n,a,b=map(int,input().split())
ans=0
for i in range(n):
    i+=1
    ii=str(i)
    cnt=0
    for j in ii:
        cnt+=int(j)
    if a<=cnt<=b:
        ans+=int(ii)
print(ans)