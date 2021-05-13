a, b, c = map(int, input().split())

if max(a, b, c) % 2 == 0:
    print(0)
else:
    print(min(a*b, min(b*c, c*a)))
