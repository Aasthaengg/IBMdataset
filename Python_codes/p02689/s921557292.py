n,m=map(int,input().split())
h=list(map(int, input().split()))
li=[[0] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    li[a-1].append(h[b-1])
    li[b-1].append(h[a-1])
ans=0
for j in range(n):
    if h[j]>max(li[j]):
        ans+=1
print(ans)