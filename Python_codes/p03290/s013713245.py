d,g = map(int,input().split())
P,C = [0]*d,[0]*d
for i in range(d): P[i],C[i] = map(int,input().split())
ans = 10**9
for bin in range(0, 1<<d):
    cnt = tot = 0
    rest_max_bit = -1
    for i in range(d):
        if bin & 1<<i:
            t = (i+1)*100
            tot += P[i]*t + C[i]
            cnt += P[i]
        else: rest_max_bit = i
    if tot >= g:
        ans = min(ans, cnt)
        continue
    if rest_max_bit < 0: continue
    t = (rest_max_bit+1)*100
    p = (g+t-tot-1)//t
    if p < P[rest_max_bit]: ans = min(ans, cnt + p)
print(ans)
