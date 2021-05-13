from fractions import Fraction

N = int(input())
A = list(map(int, input().split()))

ref = 0
for i in range(N):
    ref += Fraction(1, A[i])

ans = Fraction(1, ref)
ans = float(ans)
print(ans)
