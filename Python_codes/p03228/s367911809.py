def abk(x,y):
  if x%2==1:
    x = x-1
  y = y + x/2
  x = x/2
  return (x,y)

a,b,k = map(int, input().split())
for _ in range(k):
  if _%2==0:
    a,b = abk(a,b)
  else:
    b,a = abk(b,a)
    
a = int(a)
b = int(b)
print(a,b)