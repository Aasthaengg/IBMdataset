n,m = map(int,input().split())
l = 0
r = n+2
for i in range(m):
    a,b = map(int,input().split())
    l = max(l,a)
    r = min(r,b)
print(max(r-l+1,0))
