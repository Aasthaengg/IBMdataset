n=int(input())
a=list(map(int,input().split()))
x=sum(a)
y=0
for i in range(0,n-1):
    y+=a[i]
    if i==0:
        ans=abs(y-(x-y))
    else:
        if ans>abs(y-(x-y)):
            ans=abs(y-(x-y))
    #print(ans,y)
print(ans)