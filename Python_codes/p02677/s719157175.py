import cmath

A, B, H, M = map(int, input().split())

h = cmath.rect(A, (H / 6 + M / 360) * cmath.pi)
m = cmath.rect(B, M / 30 * cmath.pi)
print(abs(h - m))
