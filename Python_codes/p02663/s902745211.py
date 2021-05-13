h1, m1, h2, m2, k = map(int, input().split())
h = 0

m = m2 - m1
if m < 0:
    m += 60
    h -= 1
h = h2 - h1 + h
print((h * 60) + m - k)
