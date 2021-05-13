a, b = map(int, input().split())
if (a % 2 == 0 and b <= a // 2) or (a % 2 == 1 and b <= (a + 1) // 2):
  print("YES")
else:
  print("NO")