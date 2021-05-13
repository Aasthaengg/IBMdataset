from math import gcd
A, B, C, D = map(int, input().split())

def calc(X, a, b):
    return X - (X // a + X // b - X // ((a * b) // gcd(a, b)))

print(calc(B, C, D) - calc(A - 1, C, D))
