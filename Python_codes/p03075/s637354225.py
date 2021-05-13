a=[]
for i in range(5):
  k = int(input())
  a.append(k)
k = int(input())

if a[4]-a[0] <= k:
  print('Yay!')
else:
  print(':(')