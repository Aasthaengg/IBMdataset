d, g = map(int, input().split())
pc = [tuple(map(int, input().split())) for _ in range(d)]
ans = 1001001001
for s in range(1 << d):
    now = 0
    rest = g
    for i in range(d):
        if s >> i & 1:
            p, c = pc[i]
            rest -= p * (i+1) * 100 + c
            now += p
    if rest > 0:
        free = d-1
        while d >= 0 and s >> free & 1:
            free -= 1
        if free < 0:
            continue
        t = (rest + (free+1) * 100 - 1) // ((free+1) * 100)
        #print(rest,t)
        if t >= pc[free][0]:
            continue
        now += t
    ans = min(ans, now)
print(ans)