H, W = map(int, input().split())
wall = '.' * (W+2)
s = []
s.append(wall)
for i in range(H):
  tmp = "." + input() + "."
  s.append(tmp)
s.append(wall)
#for i in range(len(s)):
#  print(s[i])
for i in range(1, H+1):
  for j in range(1, W+1):
    #print(s[i][j])
    if s[i][j]=='#' and s[i-1][j]=='.' and s[i][j-1]=='.' and s[i+1][j]=='.' and s[i][j+1]=='.':
      print("No")
      exit()
print("Yes")
