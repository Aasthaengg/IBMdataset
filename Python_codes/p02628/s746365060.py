n,k=map(int,input().split())
p=sorted(map(int,input().split()))
ans=0
for i in range(k):
    ans+=p[i]
print(ans)