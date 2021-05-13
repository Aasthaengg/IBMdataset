# ABC124A

a, b = map(int, input().split())
a, b = max(a, b), min(a, b)
if a >= b + 1:
    print(2 * a - 1)
else:
    print(2 * a)
