x, y = map(int, input().split())
diff = abs(abs(x)-abs(y))
 
if abs(x) < abs(y):
  if x < 0:
    diff += 1
  if y < 0:
    diff += 1
else:
  if x > 0:
    diff += 1
  if y > 0:
    diff += 1
print(diff)