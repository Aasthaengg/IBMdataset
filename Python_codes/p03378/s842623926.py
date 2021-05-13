n,m,x=map(int,input().split())
l=[0 for i in range(n+1)]
a=list(map(int,input().split()))
for i in a:
    l[i]=1
ans=0
for i in range(x):
    ans+=l[i]
print(min(ans,sum(l)-ans))
