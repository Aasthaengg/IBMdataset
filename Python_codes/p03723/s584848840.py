A, B, C = map(int, input().strip().split())
ans = 0
while (A != B or B != C) and (A % 2) + (B % 2) + (C % 2) == 0:
  A, B, C = (B + C) // 2, (A + C) // 2, (A + B) // 2
  ans += 1
if (A % 2) + (B % 2) + (C % 2) == 0 and A == B == C:
  ans = -1
print(ans)