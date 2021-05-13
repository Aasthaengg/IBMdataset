A, B, C = map(int, input().split())
L = sorted([A, B, C])

ans = (L[1] - L[0]) / 2 + (L[2] - L[1])

if (L[0] % 2 == 1 and L[1] % 2 == 0) or (L[1] % 2 == 1 and L[0] % 2 == 0):
  ans = ans + 1.5
print(int(ans))