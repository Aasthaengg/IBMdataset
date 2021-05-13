from sys import stdin

n=int(input())
count = 0

output = 'No'

for i in range(n):
  temp = stdin.readline().split()
  if temp[0] == temp[1]:
    if count == 2:
      output = 'Yes'
      break;
    elif count == 1:
      count = 2
    elif count == 0:
      count = 1
  else:
  	count = 0
    
print(output)