k=int(input())
print(50)
if k==0:
  for i in range(50):
    print(49-i,end=" ")
    print()
else:
  a=(k-1)//50
  b=k%50
  if b==0:
    for i in range(50):
      print(50+a-i)
      print()
  else:
    for i in range(50):
      b=b-1
      if b>=0:
        print(50+a-i)
      else:
        print(50+a-i-1)
      if i==49:
        print()
