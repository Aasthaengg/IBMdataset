h1, m1, h2, m2, k = map(int, input().split())
m1 += h1 * 60
m2 += h2 * 60
print(m2 - m1 - k)
