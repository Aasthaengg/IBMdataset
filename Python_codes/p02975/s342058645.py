n = int(input())
A = list(map(int,input().split()))
Ad = {}
for a in A:
  if a not in Ad:
    Ad[a] = 1
  else:
    Ad[a] += 1
a = len(Ad)
if a == 1:
  for i in Ad.keys():
    if i == 0:
      print('Yes')
    else:
      print('No')
elif n % 3:
  print('No')
elif a == 2:
  x = 0
  for k,v in Ad.items():
    if v != n//3 and v != n//3*2:
      print("No")
      break
    else:
      x ^= k
      if v == n//3*2:
        x ^= k
  else:
    if x == 0:
      print('Yes')
    else:
      print('No')
elif a == 3:
  x = 0
  for k,v in Ad.items():
    if v != n//3:
      print("No")
      break
    else:
      x ^= k
  else:
    if x == 0:
      print('Yes')
    else:
      print('No')
else:
  print('No')
