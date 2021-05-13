a, b, c = (int(x) for x in input().split())
if a - b == 0:
    print(c)
elif a - c == 0:
    print(b)
else:
    print(a)
