from fractions import gcd
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [a//2 for a in A]

def lcm(a, b):
    return (a*b) // gcd(a, b)

k = A[0]
for a in A[1:]:
    k = lcm(a, k)

M = M - (M % k)
b = M // k


if b % 2 == 0:
    r = int(b/2)
else:
    r = int((b + 1) / 2)

for a in A[1:]:
    if k // a % 2 == 0:
        r = 0
        break

print(r)