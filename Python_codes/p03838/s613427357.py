x, y = map(int, input().split())
cnt = abs(abs(x) - abs(y))
if x * y < 0:
  cnt += 1
elif x > y:
  cnt += 2
  if x == 0 or y == 0:
    cnt -= 1
print(cnt)