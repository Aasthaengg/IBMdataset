l = map(int, raw_input().split())
a = l[0]
b = l[1]
d = a / b
r = a % b
f = float(a) / b
print d, r, round(f, 6)