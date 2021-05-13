n, a, b = map(int, input().split())
if n >= a+b:
    print(min(a, b), 0)
else:
    print(min(a, b), min(a, b)-(n-max(a, b)))
