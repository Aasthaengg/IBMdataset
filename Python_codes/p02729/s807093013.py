import math
n, m = map(int, input().split())

def combinations_count(a, b):
    return math.factorial(a+b) // (2 * math.factorial(a+b-2))

print(combinations_count(n, m)-(n*m))