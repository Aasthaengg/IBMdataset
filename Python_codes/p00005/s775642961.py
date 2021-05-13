import math

try:
    while True:
        a, b = list(map(int, input().split()))
        print("{} {}".format(math.gcd(a, b), (a * b) // math.gcd(a, b)))
except Exception as _:
    pass
