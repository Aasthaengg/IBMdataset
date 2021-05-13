h1, m1, h2, m2, s = map(int, input().split())
m = 60 * (h2 - h1) + (m2 - m1)
print(m - s)