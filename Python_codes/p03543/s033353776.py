x=list(input())
for i in range(10):
  if x.count(str(i))>=3 and x[1]==x[2]: 
    print("Yes")
    break
else:
  print("No")
