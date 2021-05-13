n, m = map(int, input().split())
s = [0] * n
t = [0] * m
for i in range(n):
    a, b = map(int, input().split())
    s[i] = (a, b)
for j in range(m):
    c, d = map(int, input().split())
    t[j] = (c, d)

for i in range(n):
    ans = 0
    mi = float('inf')
    for j in range(m):
        u = abs(s[i][0] - t[j][0]) + abs(s[i][1] - t[j][1])
        if u < mi:
            mi = u
            ans = j + 1
    print(ans)