n, ma, mb = (int(x) for x in input().split())
ABC = [tuple(int(x) for x in input().split()) for _ in range(n)]
D1 = dict()
D2 = dict()
for (m, D, j) in ((n // 2, D1, 0), (n - n // 2, D2, n // 2)):
    for bit in range(1, 1<<m):
        sum_a = 0
        sum_b = 0
        sum_c = 0
        for i in range(m):
            if bit & 1<<i:
                a, b, c = ABC[i + j]
                sum_a += a
                sum_b += b
                sum_c += c
        s = mb * sum_a - ma * sum_b
        if s in D:
            D[s] = min(D[s], sum_c)
        else:
            D[s] = sum_c
ans = 10**18
if 0 in D1:
    ans = min(ans, D1[0])
if 0 in D2:
    ans = min(ans, D2[0])
for s in D1:
    if -s in D2:
        ans = min(ans, D1[s] + D2[-s])
if ans == 10**18:
    print(-1)
else:
    print(ans)
