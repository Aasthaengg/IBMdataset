a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())
f=0
for i in [a,b,c,d,e]:
  for j in [a,b,c,d,e]:
    if abs(i-j)>k:
      f=f+1
      
if f>0:
  print(':(')
else:
  print('Yay!')