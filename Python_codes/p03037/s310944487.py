n,m = map(int,input().split())
L = []
R = []
for i in range(m):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)
ll = max(L)
rr = min(R)
print(max(0,rr-ll + 1))