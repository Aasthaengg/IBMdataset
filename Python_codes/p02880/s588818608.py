x = int(input())

for i in range(10):
  for j in range(10):
    if i*j == x:
      print('Yes')
      exit(0)

print('No')
