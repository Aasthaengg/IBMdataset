d,g = map(int,input().split())
g //= 100
P,C = [],[]
for i in range(1, d+1):
    p,c = map(int,input().split())
    P.append(p)
    C.append(c//100)
ans = 10**9
for bin in range(1, 1<<d):
    cnt = tot = 0
    for j in range(d):
        if bin & 1<<j:
            cnt += P[j]
            tot += P[j]*(j+1) + C[j]
    if tot < g: continue
    ans = min(ans, cnt)
    for j in range(d):
        if bin & 1<<j:
            rest_g = g - (tot - P[j]*(j+1) - C[j])
            p = max(0, (rest_g+j)//(j+1)) # round up
            ans = min(ans, (cnt - P[j]) + min(p, P[j]))
print(ans)
