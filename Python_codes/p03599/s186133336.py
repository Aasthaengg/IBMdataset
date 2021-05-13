a, b, c, d, e, f = map(int, input().split())

s = set()
t = set()
for i in range(0, f+1,  100 * a):
    for j in range(0, f + 1 - a, 100 * b):
        s.add(i + j)


for k in range(0, f + 1, c):
    for l in range(0, f + 1, d):
            t.add(k + l)
mi = -1
ans = [str(0), str(0)]
for n in s:
    for m in t:
        if 0 < n + m <= f and m <= n * e // 100:
            if m /(n + m) > mi:
                mi = m / (n + m)
                ans = [str(n + m), str(m)]

print(" ".join(ans))
