n=int(input())
a=[int(o) for o in input().split()]
ans=1000
stock=0
prev=0
for i in range(n-1):
    if i>0 and prev<a[i] and stock>0:
        ans+=stock*a[i]
        stock=0
    if a[i]<a[i+1]:
        m=ans//a[i]
        ans-=m*a[i]
        stock+=m
        prev=a[i]
    #print(ans," ",stock)
if  prev<a[n-1] and stock>0:
        ans+=stock*a[n-1]
print(ans)