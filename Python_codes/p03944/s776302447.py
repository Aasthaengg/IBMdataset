w,h,n=map(int,input().split())
x=[]
y=[]
a=[]
for i in range(n):
    xya=list(map(int,input().split()))
    x.append(xya[0])
    y.append(xya[1])
    a.append(xya[2])

top,bottom,left,right=h,0,0,w

for i in range(n):
    if a[i]==1:
        left=max(left, x[i])
    elif a[i]==2:
        right=min(right,x[i])
    elif a[i]==3:
        bottom=max(bottom,y[i])
    else:
        top=min(top,y[i])

if (top-bottom)<=0 or (right-left)<=0:
    ans=0
else:
    ans=(right-left)*(top-bottom)
print(ans)