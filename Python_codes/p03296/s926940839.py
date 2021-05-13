n=int(input())
a=[int(i) for i in input().split()]
b=10000
ans=0
for i in range(1,n):
    if a[i]==a[i-1]:
        a[i]=b
        ans+=1
        b-=1
print(ans)        
