N = int(input())
total = 0
for i in range(1,10):
  for j in range(1,10):
    if i*j == N:
      total =1
if total == 0:
  print('No')
else:
  print('Yes')