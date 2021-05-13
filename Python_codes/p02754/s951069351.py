n, b, r = map(int, input().split())

g = n // (b+r)
i = n % (b+r)

if b == 0:
    print(0)
elif i > b:
    print(g*b + b)
else: #i <= b
    print(g*b + i)