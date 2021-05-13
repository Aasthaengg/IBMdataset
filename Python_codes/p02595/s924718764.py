list1 = input().split(" ")
N = int(list1[0])
D = int(list1[1])
count1 = 0
for i in range(N):
  list2 = input().split(" ")
  x = int(list2[0])
  y = int(list2[1])
  d = (x**2 + y**2)**(1/2)
  if d <= D:
    count1 += 1
  else:
    pass
print(count1)  