n, m = map(int, input().split())
a, b = [], []
for _ in range(n):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)
c, d = [], []
for _ in range(m):
    c_i, d_i = map(int, input().split())
    c.append(c_i)
    d.append(d_i)
for i in range(n):
    min_idx = -1
    min_distance = 10**10
    for j in range(m):
        distance = abs(a[i]-c[j]) + abs(b[i]-d[j])
        if min_distance > distance:
            min_idx = j
            min_distance = distance
    print(min_idx + 1)