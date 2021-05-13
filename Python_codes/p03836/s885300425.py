sx, sy, tx, ty = map(int,input().split()) #n:頂点数　m:辺の数
ans = []
#(sx, sy) to (tx, ty)
for i in range(tx - sx):
  ans.append("R")
for i in range(ty - sy):
  ans.append("U")
#reverse
for i in range(tx - sx):
  ans.append("L")
for i in range(ty - sy):
  ans.append("D")
#(sx, sy) to (sx, sy - 1) to (tx + 1, sy - 1) 
#to (tx + 1, ty) to (tx, ty)
ans.append("D")
for i in range(tx - sx + 1):
  ans.append("R")
for i in range(ty - sy + 1):
  ans.append("U")
ans.append("L")
#reverse
ans.append("U")
for i in range(tx - sx + 1):
  ans.append("L")
for i in range(ty - sy + 1):
  ans.append("D")
ans.append("R")

for i in range(len(ans)):
  print(ans[i], end="")
  
