n=input()
a=''
for i in n:
  if i=='9':
    a=a+'1'
  elif i=='1':
    a=a+'9'
  else:
    a=a+i
print(int(a))