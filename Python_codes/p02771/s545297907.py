tmp = input().split(" ")
a = tmp[0]
b = tmp[1]
c = tmp[2]

if tmp.count(a) == 2 or tmp.count(b) == 2:
  print("Yes")
else:
  print("No")