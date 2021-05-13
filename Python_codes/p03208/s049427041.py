n,k=map(int,input().split())
h=[int(input()) for _ in range(n)]

h.sort()
ans=2000000000
for i in range(n):
    if i+k-1<n:
        hdif=h[i+k-1]-h[i]
        ans=min(ans,hdif)
print(ans)