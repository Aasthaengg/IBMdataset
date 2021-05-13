a, b = map(int, input().split())
c = a + b
d = a - b
e = a * b
if d <= c and e <= c:
    print(c)
elif c <= d and e <= d:
    print(d)
else:
    print(e)
