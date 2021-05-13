import copy
H,W=map(int,input().split())
List = []
for i in range (H):
  List.append(input())
resList = copy.deepcopy(List)

def bombCheck(x,y,ListX):  
  a = 0
  b = 0
  res = 0
  if ListX[x][y] == "#":
    return "#"
  for i in range(-1,2,1):
    a = x+i
    if 0<= a < H:
      for j in range(-1,2,1):
        b = y+j
        if 0<= b < W:
          if i == 0 and j ==0:
            pass
          else:
            if List[a][b] == "#":
              res +=1
  return str(res)

for i in range(H):
  resList[i] =""
  for j in range(W):
    resList[i] += bombCheck(i,j,List)
for i in resList:
  print(i)