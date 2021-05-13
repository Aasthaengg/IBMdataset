N,K=map(int,input().split())
a=list(map(int,input().split()))
d=[0]*N
ans=0
for i in range(N):
    d[a[i]-1]+=1
d.sort(reverse=True)
if len(d)>K:
    ans =sum(d[K:])
print(ans)