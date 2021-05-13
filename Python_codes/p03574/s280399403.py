h,w = map(int,input().split())
ls = []
side = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
for i in range(h):
  ls.append(list(input()))
for i in range(h):
  ans2 = ""
  for j in range(w):
    ans = 0
    if ls[i][j] == "#":
      ans2 += "#"
    else:
      for k in range(8):
        if i+side[k][0] < 0 or j+side[k][1] < 0 or h <=i+side[k][0] or w <= j+side[k][1]:
          continue
        else:
          ans += (1 if ls[i+side[k][0]][j+side[k][1]] == "#" else 0)
      ans2 += str(ans)
  print(ans2)
