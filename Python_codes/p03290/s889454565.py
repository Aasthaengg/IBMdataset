d,g = map(int,input().split())
g //= 100
P,C = [0]*d,[0]*d
for i in range(d):
    P[i],C[i] = map(int,input().split())
    C[i] //= 100
ans = 10**9
for bin in range(1, 1<<d):
    cnt = tot = 0
    for i in range(d):
        if bin & 1<<i:
            cnt += P[i]
            tot += P[i]*(i+1) + C[i]
    if tot < g: continue
    ans = min(ans, cnt)
    for i in range(d):
        if bin & 1<<i:
            rest_g = g - (tot - P[i]*(i+1) - C[i])
            p = max(0, (rest_g+i)//(i+1)) # round up
            ans = min(ans, cnt - (P[i] - p))
print(ans)
