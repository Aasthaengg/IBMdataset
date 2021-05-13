table=[]
for i in range(1,10):
  for j in range(i,10):
    table.append(i*j)
if int(input()) in table:
  print("Yes")
else:
  print("No")