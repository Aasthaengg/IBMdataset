n=int(input())

c=0
for i in range(n):
  ai=int(input())
  if ai%2!=0:
    c+=1
    break

if c==0:
  print("second")
else:
  print("first")