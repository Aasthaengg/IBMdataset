s = input()
count = 0
for i in s:
  if i == 'C' and count == 0:
    count+=1
  if i == 'F' and count == 1:
    count+=1
if count == 2:
  print("Yes")
else:
  print("No")