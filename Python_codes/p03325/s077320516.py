n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    for j in range(n):
        if a[i]%2==1:
            break
        else:
            a[i]=a[i]//2
            ans+=1
print(ans)
