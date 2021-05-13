n = int(input())
a = list(map(int,input().split()))

up=2
ans=1
for i in range(1,n):
    if up==2:
        if a[i-1]<a[i]:
            up=1
        elif a[i-1]>a[i]:
            up=0
    elif up==1 and a[i-1]>a[i]:
        up=2
        ans+=1
    elif up==0 and a[i-1]<a[i]:
        up=2
        ans+=1
        
print(ans)