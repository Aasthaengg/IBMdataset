n=int(input())

ans=[0]*(n+1)
ans[0]=2
ans[1]=1
if n>=2:
    for i in range(2,n+1):
        ans[i]=ans[i-1]+ans[i-2]
print(ans[n])