d,g = map(int,input().split())
P,C = [],[]
for i in range(1, d+1):
    p,c = map(int,input().split())
    P.append(p)
    C.append(c)
ans = 10**9
for bin in range(1, 1<<d):
    cnt = tot = 0
    for j in range(d):
        if bin & 1<<j:
            cnt += P[j]
            tot += P[j]*(j+1)*100 + C[j]
    if tot < g: continue
    ans = min(ans, cnt)
    for j in range(d):
        if bin & 1<<j:
            now_cnt = cnt
            now_tot = tot - C[j]
            for k in range(P[j]-1):
                now_cnt -= 1
                now_tot -= (j+1)*100
                if now_tot >= g: ans = min(ans, now_cnt)
print(ans)
