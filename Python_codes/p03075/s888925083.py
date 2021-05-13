ans = 0
a = [0]*6

for i in range(6):
  a[i] = int(input())

for i in range(5):
  for j in range(i+1, 5):
    if a[j] - a[i] > a[5]:
      ans = 1

if ans != 1:
  print('Yay!')
else:
  print(':(')
