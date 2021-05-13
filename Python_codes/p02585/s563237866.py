n, k = map(int, input().split())
p = list(map(int, input().split(" ")))
for i in range(n):
    p[i] -= 1
c = list(map(int, input().split(" ")))
ans = -10000000000
for start in range(n):
    now = start
    pt = 0
    cycle = 0
    looplen = 0

    while 1:
        now = p[now]
        pt += c[now]
        looplen += 1
        if now == start:
            break

    cycle = pt
    pt = 0
    for i in range(looplen):
        now = p[now]
        pt += c[now]
        aftermove = k - i-1
        if aftermove < 0:
            continue

        loop = aftermove//looplen
        ans = max(ans, pt)
        ans = max(ans, pt+loop*cycle)
print(ans)
