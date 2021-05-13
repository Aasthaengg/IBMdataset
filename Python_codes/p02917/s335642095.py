n=int(input())
b=list(map(int,input().split()))

if n==2:
    print(b[0]*2)
else:
    ans=[0]*n
    ans[0]=b[0]
    ans[n-1]=b[-1]
    for i in range(1,n-1):
        ans[i]=min(b[i],b[i-1])
    print(sum(ans))