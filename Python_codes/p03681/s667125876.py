from math import factorial
a, b = [int(i) for i in input().split()]
if abs(a-b) > 1:
    print(0)
elif a == b:
    print((2 * factorial(a) * factorial(b)) % (10 ** 9 + 7))
else:
    print((factorial(max(a, b)) * factorial(min(a, b))) % (10 ** 9 + 7))