n = int(input())
lst = []
for i in range(1,10):
  for j in range(1,10):
    a = i*j
    lst.append(a)
if (n in lst):
  print("Yes")
else:
  print("No")
