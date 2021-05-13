a,b=input().split()
a=int(a)
b=int(b)
x=10
y=int(x*8/100)
z=int(x*10/100)
i=0
while x<10000:
  if int(x*8/100)==a and int(x*10/100)==b:
    print(x)
    break
  else:
    x=x+1
if x==10000:
  print("-1")