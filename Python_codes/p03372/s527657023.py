n,c=map(int,input().split())
xy=[list(map(int,input().split())) for i in range(n)]
data=[0]*(n+1)
for i in range(n):
    x,y=xy[i]
    data[i+1]=data[i]+y
data1=[0]*(n+1)
data2=[0]*(n+1)
for i in range(n):
    x,y=xy[i]
    data1[i+1]=data[i+1]-x
    data2[i+1]=data[i+1]-2*x
data=[0]*(n+1)
for i in range(n):
    x,y=xy[n-1-i]
    data[i+1]=data[i]+y
data3=[0]*(n+1)
data4=[0]*(n+1)
for i in range(n):
    x,y=xy[n-1-i]
    data3[i+1]=data[i+1]-(c-x)
    data4[i+1]=data[i+1]-2*(c-x)
for i in range(1,n+1):
    data1[i]=max(data1[i],data1[i-1])
    data2[i]=max(data2[i],data2[i-1])
    data3[i]=max(data3[i],data3[i-1])
    data4[i]=max(data4[i],data4[i-1])
ans=-float("inf")
for i in range(0,n+1):
    a=data2[i]+data3[n-i]
    b=data4[i]+data1[n-i]
    ans=max(ans,a,b)
print(ans)