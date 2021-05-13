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
    if i == 0 or i == H-1:
      for j in range(W):
        print("#",end="")
    else:
      for j in range(W):
        if 0 < j and j < W-1:
          print(".",end="")
        else:
          print("#",end="")
    print("\n",end="")
  print("\n",end="")
