n,x=map(int,input().split())
c=0
l=list(map(int,input().split()))
for i in range(1,n):
    if(l[i-1]+l[i]>x):
        c+=l[i-1]+l[i]-x
        l[i]=max(0,l[i]-(l[i-1]+l[i]-x))
print(c)
