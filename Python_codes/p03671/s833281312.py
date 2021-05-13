a, b, c = map(int, input().split())

d = a + b
e = b + c
f = c + a
l = [d, e, f]
print(min(l))