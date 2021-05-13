a, b = map(int, input().split())
c = 0
if b>=2:
    d = b // 2
    c += d
e = b % 2
f = a * 3
g = f+e
h = g // 2
c += h
print(c)