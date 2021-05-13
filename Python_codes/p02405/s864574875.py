lines = []
colums = []

while True:
  H,W = map(int,input().split())
  if H == 0 and W == 0:
    break
  lines.append(H)
  colums.append(W)

for H,W in zip(lines,colums):
  for i in range(H):
    if i%2==0:
      for j in range(W):
        if j%2==0:
          print("#",end="")
        else:
          print(".",end="")
    else:
      for j in range(W):
        if j%2!=0:
          print("#",end="")
        else:
          print(".",end="")
      
    print("\n",end="")
  print("\n",end="")
