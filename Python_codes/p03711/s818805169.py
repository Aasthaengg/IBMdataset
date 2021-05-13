n = input().split()
x = int(n[0])
y = int(n[1])
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
if (x in a) == True and (y in a) == True:
  print('Yes')
elif (x in b) == True and (y in b) == True:
  print('Yes')
elif (x in c) == True and (y in c) == True:
  print('Yes')
else:
  print('No')
