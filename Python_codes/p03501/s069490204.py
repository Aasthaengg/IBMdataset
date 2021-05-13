n, a, b = [int(n) for n in input().split()]
p = a * n
if a * n <= b:
    print(p)
else:
    print(b)