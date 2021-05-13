a, b, c = map(int, raw_input() .split())
d = a + b
e = b + c
f = a + c
print min(d, e, f)
