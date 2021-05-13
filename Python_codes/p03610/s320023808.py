a=input()
b=""
if int(len(a))%2==0:
  for i in range(int(len(a)/2)):
    b=b+a[2*i]
  print(b)
else:
  for i in range(int(len(a)/2)+1):
    b=b+a[2*i]
  print(b)