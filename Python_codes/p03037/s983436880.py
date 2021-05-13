n,m = list(map(int,input().split()))
la = 0
ra = n
for i in range(m):
    l,r=list(map(int,input().split()))
    la = max(la,l)
    ra = min(ra,r)
print(max(0,ra-la+1))
