a=[]
for i in range(6):
  a.append(int(input()))
b=a.pop(5)
a=sorted(a)
if abs(a[0]-a[4])>b:
  print(':(')
else:
  print('Yay!')
