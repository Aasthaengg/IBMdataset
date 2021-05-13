n,k=map(int,input().split())
h=[int(input()) for i in range(n)]
h.sort()
ans=h[k-1]-h[0]
res=float("INF")
for i in range(n-k+1):
    res=h[i+k-1]-h[i]
    if ans>res:
        ans=res
print(ans)
