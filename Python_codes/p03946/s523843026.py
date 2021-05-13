n,t=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]

c=0
dif=0
m=a[0]
for i in range(1,n):
    if(m>a[i]):
        m=a[i]
    if(dif<a[i]-m):
        c=1
        dif=a[i]-m
    elif(dif==a[i]-m):
        c+=1
print(c)