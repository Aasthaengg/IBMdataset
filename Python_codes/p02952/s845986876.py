n = int(input())
m = len(str(n))
if m == 1:
  print(n)
elif m == 2:
  print(9)
elif m == 3:
  print(9 + n - 99)
elif m == 4:
  print(909)
elif m == 5:
  print(909 + n -9999)
else:
  print(90909)