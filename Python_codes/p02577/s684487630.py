string = input()
sum = 0

for i in range(len(string)):
  sum += int(string[i])

if sum % 9 == 0:
  print('Yes')
else:
  print('No')
