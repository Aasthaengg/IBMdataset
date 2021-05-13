from math import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


N = int(input())
A = list(map(int, input().split()))
X = A[0]

for a in A[1:]:
    X = lcm(X, a)
X -= 1
ans = 0
for a in A:
    ans += X % a
print(ans)