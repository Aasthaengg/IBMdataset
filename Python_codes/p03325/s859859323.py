n=int(input())
a=list(map(int,input().split()))

ans=0
for i in range(n):
    flag=True
    while flag:
        if a[i]%2==0:
            a[i]=a[i]/2
            ans+=1
        else:
            flag=False
print(ans)
