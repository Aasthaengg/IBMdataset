h, w = map(int, input().split(" "))
s = []
s.append(["0"] * (w + 2))
for i in range(h):
  s.append(list("0"+input().replace(".","0").replace("#","1")+"0"))
s.append(["0"] * (w + 2))

ans = []
for i in range(1, h + 1):
  tmp = []
  for j in range(1, w + 1):
    if s[i][j] == "1":
      tmp.append("#")
    else:
      tmp2 = ""
      tmp2 += s[i-1][j-1]
      tmp2 += s[i-1][j]
      tmp2 += s[i-1][j+1]
      tmp2 += s[i][j-1]
      tmp2 += s[i][j+1]
      tmp2 += s[i+1][j-1]
      tmp2 += s[i+1][j]
      tmp2 += s[i+1][j+1]
      tmp.append(tmp2.count("1"))
  ans.append(tmp)

for i in range(h):
  for j in range(w):
    print(ans[i][j], end="")
  print()