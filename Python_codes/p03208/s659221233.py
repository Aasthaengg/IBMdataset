n,k=map(int,input().split())
h=[int(input()) for _ in range(n)]
h.sort()
ans=float('inf')
for i in range(n-k+1):
    tmp=h[i+k-1]-h[i]
    ans=min(tmp,ans)
print(ans)