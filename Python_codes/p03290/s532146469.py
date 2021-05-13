d, g = map(int, input().split())
p = [0 for _ in range(d)]
c = [0 for _ in range(d)]
for i in range(d):
    p[i], c[i] = map(int, input().split())
ans = -1
for pat in range(2**d):
    score = 0
    now = 0
    l = []
    for i in range(d):
        if pat & (2 ** i):
            l.append(i)
            score += 100*(i+1)*p[i]+c[i]
            now += p[i]
    if score < g:
        maxidx = None
        for i in range(d-1, -1, -1):
            if not i in l:
                maxidx = i
                break
        if maxidx == None:
            continue
        if score+100*(maxidx+1)*(p[maxidx]-1) < g:
            continue
        for i in range(p[maxidx]-1):
            score += 100*(maxidx+1)
            now += 1
            if score >= g:
                break
    if ans == -1 or ans > now:
        ans = now
print(ans)