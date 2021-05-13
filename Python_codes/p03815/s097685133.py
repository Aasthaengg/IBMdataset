x = int(input())

cnt = (x // 11) * 2
if x % 11 == 0:
  print(cnt)
elif x % 11 <= 6:
  print(cnt + 1)
else:
  print(cnt + 2)