
n=int(input())
p=[0]*n
for i in range(n):
    p[i]=int(input())

a=[0]*n
cnt=1
ans=0
for i in range(n):
    a[p[i]-1]=i
#print('n,p=',n,p,a)
for i in range(n):
    if i==0:
        pre=a[0]
    else:
        if a[i]>pre:
            cnt+=1
        else:
            ans=max(ans,cnt)
            cnt=1
    ans=max(ans,cnt)
    pre=a[i]
print(n-ans)
