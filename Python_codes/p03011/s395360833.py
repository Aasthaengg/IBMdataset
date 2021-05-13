a, b, c = [int(i) for i in input().split()]
d = a + b
e = a + c
f = b + c
print(min(d, e, f))