p, q, r = map(int, input().split())
a = p + q
b = q + r
c = r + p
print(min(a, b, c))
