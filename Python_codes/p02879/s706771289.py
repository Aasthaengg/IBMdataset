a = input().split()
if int(a[0]) > 9 or int(a[1]) >9:
  print("-1")
else:
  print(int(int(a[0]) * int(a[1])))