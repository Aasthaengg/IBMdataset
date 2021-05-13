x=int(input())
ma=1
for i in range(2,x):
  ex=i**2
  for j in range(x):
    if ex*i>x:
      if ex>ma and ex<=x:
        ma=ex
      break
    ex=ex*i
print(ma)