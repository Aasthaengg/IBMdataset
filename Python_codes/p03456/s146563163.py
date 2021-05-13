a,b=map(int,input().split())
for i in range(1,400):
  if i**2==int(str(a)+str(b)):
    print("Yes")
    break
else:
  print("No")