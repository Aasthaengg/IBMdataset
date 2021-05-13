n = input()
if int(n) in [10 ** i for i in range(1, 6)]:
  print(10)
else:
  res = 0
  for i in range(len(n)):
    res += int(n[i])
  print(res)