a, b = map(int, input().split())
ans = 0
if a > b:
  for i in range(1, a + 1):
    if b * i % a == 0:
      ans = b * i
      break
else:
  for i in range(1, b + 1):
    if a * i % b == 0:
      ans = a * i
      break
print(ans)
