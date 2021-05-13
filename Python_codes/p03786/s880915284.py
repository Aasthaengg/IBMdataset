n=int(input())
a=sorted(list(map(int,input().split())))
now=a[0]
ans=1
for i in range(1,n):
    if now*2>=a[i]:
        ans+=1
    else:
        ans=1
    now+=a[i]
print(ans)