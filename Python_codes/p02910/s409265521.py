s = input()
a = 1
f = 0
for i in s:
  if a == 1 and i == "L":
    print("No")
    f = 1
    break
  if a == 0 and i == "R":
    print("No")
    f = 1
    break
  a ^= 1
if f == 0:
  print("Yes")