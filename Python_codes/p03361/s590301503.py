import sys
h, w = map(int, input().split())
l = [list(input()) for i in range(h)]
for i in range(h):
  l[i] = ["."] + l[i] + ["."]
l = [["." for i in range(w+2)]] + l + [["." for i in range(w+2)]]
for i in range(1, h+1):
  for j in range(1, w+1):
    if l[i][j] == "#":
      if "#" not in [l[i-1][j], l[i][j-1], l[i][j+1], l[i+1][j]]:
        print("No")
        sys.exit()
print("Yes")