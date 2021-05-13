input()
hat = input()
num = 0
for i in hat:
  if i == "R":
    num += 1
if num > (len(hat)/2):
  print("Yes")
else:
  print("No")