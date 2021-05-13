import math
K = int(input())

odd = list(range(1, K+1, 2))
even = list(range(2, K+1, 2))


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


print(combinations_count(len(odd), 1)*combinations_count(len(even), 1))
