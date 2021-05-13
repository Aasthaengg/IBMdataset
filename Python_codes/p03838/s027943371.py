x, y = map(int, input().split())
if y > 0:
  if x < - y:
    ans = - y - x + 1
  elif -y <= x < 0:
    ans = y + x + 1
  elif 0 <= x <= y:
    ans = y - x
  else:
    ans = x - y + 2
elif y < 0:
  if x < y:
    ans = y - x
  elif y <= x < 0:
    ans = - y + x + 2
  elif 0 <= x <= - y:
    ans = - y - x + 1
  else:
    ans = y + x + 1
else:
  if x <= 0:
    ans = abs(x)
  else:
    ans = x + 1

print(ans)