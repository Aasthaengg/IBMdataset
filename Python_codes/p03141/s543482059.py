n = int(input())
d = {}
i = 0
x, s = [], []
for _ in range(n):
    a, b = map(int, input().split())
    k = a + b
    if not k in d:
        d[k] = i
        x.append([])
        s.append(k)
        i += 1
    x[d[k]].append([a, b])
t, a = 0, 0
s.sort(reverse = True)
l = len(x)
for i in range(l):
    x[i].sort(reverse = True)
now = 1
ans = 0
for i in s:
    y = x[d[i]]
    i, j = 0, len(y) - 1
    while i <= j:
        if now:
            ans += y[i][0]
            i += 1
        else:
            ans -= y[j][1]
            j -= 1
        now ^= 1
print(ans)