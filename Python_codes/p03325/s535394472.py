N=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(N):
    if a[i]%2==0:
        tmp=a[i]
        while tmp%2==0:
            tmp=tmp//2
            ans+=1
print(ans)