import sys
a=list(map(int,open(0).read().split()))
for i in range(5):
  for j in range(5):
    if i==j:
      continue
    elif abs(a[i]-a[j])>a[5]:
      print(':(')
      sys.exit()
else:
  print('Yay!')