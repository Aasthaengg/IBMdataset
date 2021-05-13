n,m = map(int,input().split())
l,r = [],[]
for i in range(m):
    a,b = map(int,input().split())
    l.append(a)
    r.append(b)
num = list(range(1,n+1))
lmax = max(l)
rmin = min(r)
if lmax > rmin:
    print(0)
else:
    gate = set(range(lmax,rmin+1))
    ans = list(set(num) & gate)
    print(len(ans))