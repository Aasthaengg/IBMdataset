d,g = map(int,input().split())
P,C = [0]*d,[0]*d
for i in range(d): P[i],C[i] = map(int,input().split())
ans = 10**9
for bin in range(1, 1<<d):
    cnt = tot = 0
    for i in range(d):
        if bin & 1<<i:
            cnt += P[i]
            tot += P[i]*(i+1)*100 + C[i]
    if tot < g: continue
    ans = min(ans, cnt)
    for i in range(d):
        if bin & 1<<i:
            now_cnt = cnt
            now_tot = tot - C[i]
            for k in range(P[i]-1):
                now_cnt -= 1
                now_tot -= (i+1)*100
                if now_tot >= g: ans = min(ans, now_cnt)
print(ans)
