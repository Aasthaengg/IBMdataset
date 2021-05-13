a, b, c = map(int, input().split())
d = a + b
e = b + c
f = c + a
print(min(d,e,f))