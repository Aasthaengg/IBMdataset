x, y = map(int, input().split())
if x >= 0 and y >= 0 and x <= y:
  ans = y - x
elif x >= 0 and y > 0 and x >= y:
  ans = x -  y + 2
elif x <= 0 and y <= 0 and x <= y:
  ans = y - x
elif x < 0 and y <= 0 and x >= y:
  ans = x - y + 2
elif x >= 0 and y <= 0:
  ans = abs(x - abs(y)) + 1
elif x <= 0 and y >= 0 and abs(x) <= y:
  ans = y - abs(x) + 1
elif x <= 0 and y >= 0 and abs(x) > y:
  ans = abs(x) - y + 1
print(ans)