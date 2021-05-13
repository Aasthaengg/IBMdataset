N=int(input())
S=list(str(input()))
x=0
x_max=0
for i in S:
  if i=='I':
    x+=1
    if x>x_max:
      x_max=x
  else:
    x-=1
print(x_max)