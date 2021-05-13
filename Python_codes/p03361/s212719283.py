h, w = map(int, input().split())
mat = []
mat.append("."*(w+2))
for i in range(h):
  s = input()
  mat.append("."+s+".")
mat.append("."*(w+2))

for x in range(1,w+1):
  for y in range(1, h+1):
    if mat[y][x] == "#" and mat[y-1][x] == "." and mat[y+1][x] == "." and mat[y][x-1] == "." and mat[y][x+1] == ".":
      print("No")
      exit()
print("Yes")