s = [i **2 for i in range(1, 1000)]
a, b = input().split()
if int(a+b) in s:
  print("Yes")
else:
  print("No")