N=int(input())
a=list(map(int,input().split()))
num=1
ans=0
for i in range(1,N):
    if a[i]==a[i-1]:
        num+=1
    else:
        ans+=num//2
        num=1
ans+=num//2
print(ans)