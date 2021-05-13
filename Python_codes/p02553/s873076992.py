read = lambda: list(map(int, input().split()))

a, b, c, d = read()

p = a * c
q = a * d
r = b * c
s = b * d
print(max(p, q, r, s))