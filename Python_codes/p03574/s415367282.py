h,w=map(int, input().split())
mat = []
mat.append(["."]*(w+2))
for i in range(h):
  mat.append(["."]+list(input())+["."])
mat.append(["."]*(w+2))
for y in range(1, h+1):
  for x in range(1, w+1):
    if mat[y][x] != "#":
      c = 0
      if mat[y-1][x-1] == "#":
        c += 1
      if mat[y-1][x] == "#":
        c += 1       
      if mat[y-1][x+1] == "#":
        c += 1      
      if mat[y][x-1] == "#":
        c += 1
      if mat[y][x+1] == "#":
        c += 1
      if mat[y+1][x-1] == "#":
        c += 1        
      if mat[y+1][x] == "#":
        c += 1        
      if mat[y+1][x+1] == "#":
        c += 1
      mat[y][x] = str(c)

for y in range(1, h+1):
  print("".join(mat[y][1:w+1]))
        
