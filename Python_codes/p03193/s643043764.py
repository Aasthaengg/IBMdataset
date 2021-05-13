n,h,w=map(int, input().split())
a=[list(map(int, input().split())) for num in range(n)]
ans=0

for num in range(n):
    cut=int(a[num][0]/h)
    cutw=int(a[num][1]/w)
    if cut==0 or cutw==0:
        cut=0
        cutw=0
    if cutw<cut:
        cut=cutw
    ans+=cut
    
print(ans)