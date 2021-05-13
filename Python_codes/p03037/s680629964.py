n,m = map(int,input().split())
l = []
r = []

for i in range(m):
    l_t,r_t = map(int,input().split())
    l.append(l_t)
    r.append(r_t)

print(max(min(r)-max(l)+1,0))
