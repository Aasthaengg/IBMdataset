A, B = map(int, input().split())
if A > B:
  A, B = B, A
if abs(A - B) % 2 != 0:
  print("IMPOSSIBLE")
  exit()
print(A + (abs(A-B) // 2))