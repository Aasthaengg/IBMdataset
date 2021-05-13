h,w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
  for j in range(w):
    if s[i][j] == "#":
      if i != 0: # 上
        if s[i-1][j] == "#": continue
      if i != h-1: #下
        if s[i+1][j] == "#": continue
      if j != 0: #左
        if s[i][j-1] == "#": continue
      if j != w-1: #右
        if s[i][j+1] == "#": continue
      print("No")
      exit()
print("Yes")