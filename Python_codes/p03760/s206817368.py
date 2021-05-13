a=input()
b=input()
x=''
for i in range(len(b)):
  x+=a[i]
  x+=b[i]
if len(a)==len(b):
  print(x)
else:
  print(x+a[-1])