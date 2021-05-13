a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lists = [a,b,c,d,e]
lists_2 = [a%10,b%10,c%10,d%10,e%10]
for i in range(4):
  if 0 in lists_2:
    lists_2.remove(0)
  else:
    pass

count = 0
counter = 0
for i in lists:
  if i%10 == 0:
    count += i
  elif i%10!= min(lists_2):
    count += ((i//10) +1)*10
  else:
    if counter == 0:
      count += i
      counter = 1
    else:
      count += ((i//10) +1)*10
print(count)