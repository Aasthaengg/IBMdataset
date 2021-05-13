x=list(input())
for i in x:
  if x.count(i)!=2:
    print("No")
    break
else:
  print("Yes")