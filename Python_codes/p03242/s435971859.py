a=list(input())
for i in range(3):
  if int(a[i])==1:
    a[i]='9'
  elif int(a[i])==9:
    a[i]='1'
print(''.join(a))