import math

a, b = map(int, input().split())


def choice(n, r):
    if r > n:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


print(choice(a, 2) + choice(b, 2))