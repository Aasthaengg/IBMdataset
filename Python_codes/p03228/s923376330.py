def change(x,y):
  if x%2==1:
    x-=1
  x=x//2
  y+=x
  return x,y
a,b,k=map(int,input().split())
for i in range(k):
  if i%2==0:
    a,b=change(a,b)
  else:
    b,a=change(b,a)
print(a,b)