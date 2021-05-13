N = int(input())
count = 0
for i in range(26):
  for j in range(15):
    if i*4 + j*7 == N:
      count +=1
if count > 0:
  print('Yes')
else:
  print('No')