from fractions import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


N = int(input())
A = list(map(int, input().split()))
LCM = A[0]
for i in range(1, N):
    LCM = lcm(LCM, A[i])
print(sum((LCM - 1) % a for a in A))
