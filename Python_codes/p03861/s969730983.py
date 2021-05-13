a,b,x = map(int, input().split())
right = b // x + 1
if a == 0:
  left = 0
else:
  left = (a - 1) // x + 1
print(right - left)
