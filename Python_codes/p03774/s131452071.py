n, m = map(int, input().split())
a, b, c, d = [0] * n, [0] * n, [0] * m, [0] * m
for i in range(n):
    a[i], b[i] = map(int, input().split())
for i in range(m):
    c[i], d[i] = map(int, input().split())

for i in range(n):
    min_dist, min_c = 10**9, -1
    for j in range(m):
        dist = abs(a[i]-c[j]) + abs(b[i]-d[j])
        if dist < min_dist:
            min_dist = dist
            min_c = j
    print(min_c+1)