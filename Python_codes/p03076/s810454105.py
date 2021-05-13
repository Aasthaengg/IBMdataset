import math
count = 0
amari = 10
for i in range(5):
  n = int(input())
  if n%10 == 0:
    count += n
  else:
    count += math.ceil(n/10)*10
    amari = min(amari,n%10)
if amari %10 == 0:
  print(count + amari - 10) 
else:
  print(count + amari -10)