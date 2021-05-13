n,m=map(int,input().split())
ans=[-1]*n

for i in range(m):
    s,c=map(int,input().split())
    s-=1
    if ans[s]>=0 and ans[s]!=c:
        print(-1)
        exit()

    ans[s]=c
if ans[0]==-1:
    if n>=2:
        ans[0]=1
    else:
        ans[0]=0
if ans[0]==0 and n!=1:
    print(-1)
    exit()
for i in range(1,n):
    if ans[i]==-1:
        ans[i]=0
x=0
for i in range(n):
    x+=ans[-1-i]*(10**i)
print(x)
