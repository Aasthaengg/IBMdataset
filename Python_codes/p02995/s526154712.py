from math import gcd
A, B, C, D = map(int, input().split())

if C == 1 or D == 1:
    print(0)
    exit()

def check(A, B, x):
    return B//x - (A-1)//x

print((B - A + 1) - (check(A, B, C) + check(A, B, D) - check(A, B, C*D//gcd(C, D))) )
