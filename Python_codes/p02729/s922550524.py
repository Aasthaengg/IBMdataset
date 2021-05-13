N, M = map(int, input().split())

from math import factorial

def combination(n, r):
    if n < 2:
        return 0
    else:
        return factorial(n) // (factorial(n - r)*factorial(r))

print("{}".format(combination(N, 2) + combination(M, 2)))
