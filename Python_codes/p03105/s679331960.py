a, b, c = map(int, input().split())

total = a * c

if b >= total:
    print(c)
else:
    print(b // a)