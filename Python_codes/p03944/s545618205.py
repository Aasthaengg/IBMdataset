w,h,n=map(int,input().split())
c=[]
for i in range(n):
    x,y,a=map(int,input().split())
    c.append([x,y,a])
s=w*h
ans=0
for j in range(s):
    x=j%w
    y=j//w
    t=0
    for i in range(n):
        if c[i][2]==1:
            if x<c[i][0]:
                t+=1
                break
        if c[i][2]==2:
            if x>=c[i][0]:
                t+=1
                break
        if c[i][2]==3:
            if y<c[i][1]:
                t+=1
                break
        if c[i][2]==4:
            if y>=c[i][1]:
                t+=1
                break
    if t==0:
        ans+=1
print(ans)