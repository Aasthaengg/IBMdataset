n,c=[int(j) for j in input().split()]
xv=[]
for i in range(n):
    xv.append([int(j) for j in input().split()])
ll=[[xv[0][0],max(0,xv[0][1]-xv[0][0])]]
lr=[[c-xv[-1][0],max(0,xv[-1][1]-c+xv[-1][0])]]
tmp=xv[0][1]
for i in range(1,n):
    x,v=xv[i]
    tmp+=v
    ll.append([x,max(tmp-x,ll[-1][1])])
tmp=xv[-1][1]
for i in range(n-1)[::-1]:
    x,v=xv[i]
    x=c-x
    tmp+=v
    lr.append([x,max(tmp-x,lr[-1][1])])
ans=0
for i in range(n+1):
    if i==0:
        ans=max(ans,lr[n-1][1])
    elif i==n:
        ans=max(ans,ll[n-1][1])
    else:
        ans=max(ans,ll[i-1][1]+lr[n-i-1][1]-ll[i-1][0])
        ans=max(ans,ll[i-1][1]+lr[n-i-1][1]-lr[n-i-1][0])

print(ans)




