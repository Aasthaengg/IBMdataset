n = input()

"""max(n) = 100000"""
if len(n) == 6:
  res = 9 + 900 + 90000
  print(res)
elif len(n) == 5:
  res = 9 + 900 + (int(n) -9999)
  print(res)
elif len(n) == 4:
  res = 9 + 900
  print(res)
elif len(n) == 3:
  res = 9 + (int(n) - 99)
  print(res)
elif len(n) == 2:
  res = 9
  print(res)
else:
  res = int(n)
  print(res)