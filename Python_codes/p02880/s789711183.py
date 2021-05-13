num = int(input())

n = 1
while n < 10:
  if num % n == 0 and num // n < 10:
    print('Yes')
    break
    
  n += 1
    
if n == 10:
  print('No')