number = int(input())
list = []
count = 0
num = 0

for i in range(number):
  x, y = input().split()
  list.append(x)
  list.append(y)
 

for num in range(0,len(list)-1,2):
  if list[num] == list[num+1]:
    count += 1
    if count == 3:
      break
  else:
    count = 0 

if count < 3:
  print("No")
else:
  print("Yes")
