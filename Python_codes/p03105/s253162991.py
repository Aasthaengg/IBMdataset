a, b, c = list(map(int, input().split()))

if (c*a) <= b:
    print(c)
else:
    print(b//a)