a,b,c = map(int, input().split())
if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
  print(0)
else:
  for i in range(10**6):
    temp1 = a
    temp2 = b
    temp3 = c
    a = int((temp2+temp3)/2)
    b = int((temp1+temp3)/2)
    c = int((temp1+temp2)/2)
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
      break
  if i == 10**6 - 1:
    print(-1)
  else:
    print(i+1)