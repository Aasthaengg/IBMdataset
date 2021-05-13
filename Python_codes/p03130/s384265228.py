list1 =[]
total =0
for i in range(3):
  MM = input().split()
  a = int(MM[0])
  b = int(MM[1])
  list1.append(a)
  list1.append(b)
for i in range(5):
  x = list1.count(i)
  if x >2:
    total +=1
if total == 0:
  print('YES')
else:
  print('NO')