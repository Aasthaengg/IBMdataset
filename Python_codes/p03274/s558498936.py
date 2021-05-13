n,k = map(int,input().split())
a = list(map(int,input().split()))

p = []
m = []
for i in a:
    if i >= 0:
        p.append(i)
    else:
        m.insert(0,-i)
p.insert(0,0)
m.insert(0,0)

ans = 10**9
for i in range(k+1):
    if i < len(p) and k-i < len(m):
        d_p = p[i]
        d_m = m[k-i]
        d = min(d_p,d_m)*2 + max(d_p,d_m)
        ans = min(ans,d)

print(ans)