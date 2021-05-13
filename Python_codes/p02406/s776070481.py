n = int(input())
for i in range(3, n + 1):
  if i % 3 == 0 or i % 10 == 3 or '3' in str(i):
      print('',"{0}".format(i),end='')
print()