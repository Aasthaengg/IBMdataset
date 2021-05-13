a, b = map(int, input().split())
c = a + b
if c < 24:
    print(c)
else:
    c -= 24
    print(c)
