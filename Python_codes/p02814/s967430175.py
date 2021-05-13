import math

N, M = [int(_) for _ in input().split()]

A = [int(_) for _ in input().split()]

for i in range(N):
    a = A[i]
    if a % 2 > 0:
        print(0)
        exit()
    A[i] = a // 2


def f(v):
    res = 0
    while v % 2 == 0:
        res += 1
        v //= 2
    return res


c = f(A[0])
for i in range(N):
    if c != f(A[i]):
        print(0)
        exit()
    if c > 0:
        A[i] <<= c

if c > 0:
    M <<= c


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


l = 1
for a in A:
    l = lcm(l, a)
if l > M:
    print(0)
    exit()
print((M // l + 1) // 2)
