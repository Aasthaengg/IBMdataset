lst = sorted(list(map(int, input().split())), reverse=True)
diff = lst[0] * 2 - lst[1] - lst[2]
if diff % 2 == 0:
  print(diff // 2)
else:
  print(diff // 2 + 2)