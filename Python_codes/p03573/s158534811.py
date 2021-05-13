# A - One out of Three
a, b, c = [int(s) for s in input().split()]

if a == b:
    print(c)
elif b == c:
    print(a)
elif c == a:
    print(b)