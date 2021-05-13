d, g = map(int, input().split())
g //= 100
p = [0] * d
c = [0] * d
for i in range(d):
    p[i], c[i] = map(int, input().split())
    c[i] //= 100
ans = 10000000
for i in range(1 << d):
    s = set()
    use = 0
    res = 0
    for j in range(d):
        if i >> j & 1:
            use += p[j]
            res += p[j] * (j + 1) + c[j]
            s.add(j)
    for j in range(d - 1, -1, -1):
        if res >= g:
            break
        if j in s:
            continue
        use += min(p[j], (g - res + j) // (j + 1))
        res += min(p[j], (g - res + j) // (j + 1)) * (j + 1)
    if res >= g:
        ans = min(ans, use)
print(ans)
