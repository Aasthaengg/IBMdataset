n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

m = sum(a)
s = set()
i = 1
while i * i <= m:
    if m % i == 0:
        s |= set([i, m // i])
    i += 1

ans = 0
for i in s:
    b = [j % i for j in a]
    b.sort()
    c = [0]
    for j in b:
        c.append(c[-1] + j)
    d = [0]
    for j in reversed(b):
        d.append(d[-1] + (i-j))
    d = list(reversed(d))

    for j in range(n+1):
        if (c[j] - d[j]) % i == 0:
            if max(c[j], d[j]) <= k:
                ans = max(ans, i)
print(ans)
