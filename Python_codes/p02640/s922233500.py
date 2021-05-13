a,b=input().split()
a=int(a)
b=int(b)
c=0
for i in range(a+1):
  if 2*i+4*(a-i)==b:
    c=c+1
if c==0:
  print("No")
else:
  print("Yes")