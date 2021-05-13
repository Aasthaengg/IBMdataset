h,w = map(int, input().split(" "))
temp = [list(input()) for i in range(h)]

a = [["." for i in range(w + 2)] for j in range(h + 2)]
for i in range(h):
  for j in range(w):
    a[i + 1][j + 1] = temp[i][j]

for i in range(1, h + 2):
  for j in range(1, w + 2):
    if a[i][j] == "#":
      if a[i - 1][j] != "#" and a[i + 1][j] != "#" and a[i][j - 1] != "#" and a[i][j + 1] != "#":
        print("No")
        break
  else:
    continue
  break
else:
  print("Yes")