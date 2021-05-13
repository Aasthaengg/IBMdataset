A = int(input())
for i in range(3, A + 1):
  if i%3 == 0 or i%10 == 3 or '3' in str(i):
    print('', i , end = '')
print()