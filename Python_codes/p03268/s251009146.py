n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
    if 2*i%k==0:
        ans+=(1+(n+i)//k+(-1-i)//k)**2
print(ans)