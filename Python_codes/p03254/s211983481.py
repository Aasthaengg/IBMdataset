n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(n):
    if x>=a[i]:
        x-=a[i]
        ans+=1
    else:
        break
else:
    if x>0:
        ans-=1
print(ans)