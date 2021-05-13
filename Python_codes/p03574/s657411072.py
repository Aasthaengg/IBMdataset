h, w = map(int, input().split(" "))
s = []
s.append(["."] * (w + 2))
for i in range(h):
  s.append(list("."+input()+"."))
s.append(["."] * (w + 2))

for i in range(1, h + 1):
  for j in range(1, w + 1):
    if s[i][j] != "#":
      tmp = ""
      tmp += s[i-1][j-1]+s[i-1][j]+s[i-1][j+1]
      tmp += s[i][j-1]+s[i][j+1]
      tmp += s[i+1][j-1]+s[i+1][j]+s[i+1][j+1]
      s[i][j] = str(tmp.count("#"))

for i in range(1, h + 1):
  for j in range(1, w + 1):
    print(s[i][j], end="")
  print()