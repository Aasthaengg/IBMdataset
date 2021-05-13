import math


def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N, P = map(int, input().split())
A = list(map(int, input().split()))

odd = 0
even = 0
for a in A:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1

ans = 0
for i in range(P, odd+1, 2):
    tmp = combination(odd, i)
    for j in range(0, even+1):
        ans += tmp * combination(even, j)
print(ans)
