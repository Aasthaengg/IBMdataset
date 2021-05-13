h1, m1, h2, m2, k = map(int, input().split())
t = 0

if h1 == h2:
    t = m2 - m1
else:
    if m2 >= m1:
        t = (h2 - h1) * 60 + m2 - m1
    else:
        t = (h2 - h1 -1) * 60 + m2 +60 - m1
print(t - k)