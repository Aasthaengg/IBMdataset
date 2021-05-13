N = int(input())
SS = input().split()
list1 = [int(i) for i in SS]
list1.sort(reverse = True)
total = 0
maxi = list1.pop(0)
for i in list1:
  total +=i

if total > maxi :
  print('Yes')
else:
  print('No')