L,R,d=map(int,input().split())
a=L//d
b=R//d
c=L%d
if c==0:
  print(b-a+1)
else:
  print(b-a)