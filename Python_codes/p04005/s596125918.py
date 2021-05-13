a, b, c = map(int, input().split())
if any(x % 2 == 0 for x in (a, b, c)):
    print(0)
else:
    print(min(a*b, b*c, c*a))
