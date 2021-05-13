a = input().split()
a = [int(i) for i in a]
if a[1] == 1:
  print(0)
else:
  print(a[0]-a[1])