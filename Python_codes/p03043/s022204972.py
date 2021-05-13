from fractions import Fraction
N, K = map(int, input().split())
ans = 0
for i in range(N):
    s = i + 1
    p = Fraction(1, N)
    while s < K:
        s *= 2
        p *= Fraction(1, 2)
    ans += p
print(float(ans))
