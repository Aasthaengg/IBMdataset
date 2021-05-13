lst = sorted(list(map(int, input().split())))
if lst[1] - lst[0] >= 1:
  print(lst[1] * 2 - 1)
else:
  print(2 * lst[1])