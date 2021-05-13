inp = input()
inpa = input()

rsum = 0
for i in range(int(inp)):
  if inpa[i] == "R":
    rsum = rsum + 1
    
if rsum > int(inp)/2:
      print("Yes")
else:
  print("No")