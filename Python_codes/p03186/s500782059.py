A, B, C = map(int, input().split())
if B >= C:
  print(B+C)
  exit()
if A + B >= C:
  print(C + B)
  exit()
print(A + B + B + 1)