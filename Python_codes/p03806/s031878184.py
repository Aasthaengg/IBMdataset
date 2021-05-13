n, ma, mb = (int(x) for x in input().split())
ABC = [tuple(int(x) for x in input().split()) for _ in range(n)]
m = n // 2
D = dict()
E = dict()
for bit in range(1, 1<<m):
    sum_a = 0
    sum_b = 0
    sum_c = 0
    for i in range(m):
        if bit & 1<<i:
            a, b, c = ABC[i]
            sum_a += a
            sum_b += b
            sum_c += c
    s = mb * sum_a - ma * sum_b
    if s in D:
        D[s] = min(D[s], sum_c)
    else:
        D[s] = sum_c

k = n - m
for bit in range(1, 1<<k):
    sum_a = 0
    sum_b = 0
    sum_c = 0
    for i in range(k):
        if bit & 1<<i:
            a, b, c = ABC[m + i]
            sum_a += a
            sum_b += b
            sum_c += c
    s = mb * sum_a - ma * sum_b
    if s in E:
        E[s] = min(E[s], sum_c)
    else:
        E[s] = sum_c

ans = 10**18
if 0 in D:
    ans = min(ans, D[0])
if 0 in E:
    ans = min(ans, E[0])
for s, c in D.items():
    if -s in E:
        ans = min(ans, D[s] + E[-s])
if ans == 10**18:
    print(-1)
else:
    print(ans)
