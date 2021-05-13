n,k=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
ans=0
for i in range(k):
    ans+=l[-i-1]
print(ans)
