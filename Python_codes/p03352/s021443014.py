x = int(input())
ans = 0
for a in range(2, 33):
  for b in range(2, 10):
    if a**b > x:
      break
    ans = max(ans, a**b)
print(max(ans, 1))