import numpy as np
H, W = map(int, input().split())
map_lis = [input() for i in range(H)]
ans = 0

def prob(x,y,h,w):
  if 0<=x<h and 0<=y<w:
    return True
  else:
    return False

def count(x,y,lis):
  if not lis[x][y]:
    return True
  else:
    return False

def maze(x,y,lis):
  if lis[x][y] == ".":
    return True
  else:
    return False

for i in range(H):
  for j in range(W):
    k = 0
    count_lis = np.zeros((H,W))
    num_lis = [[] for i in range(1000)]
    if maze(i,j,map_lis):
      count_lis[i][j] = 1
      num_lis[0].append([i,j])
    while True:
      for l in num_lis[k]:
        if prob(l[0]-1,l[1],H,W) and count(l[0]-1,l[1],count_lis) and maze(l[0]-1,l[1],map_lis):
          num_lis[k+1].append([l[0]-1,l[1]])
          count_lis[l[0]-1][l[1]] = 1
        if prob(l[0],l[1]-1,H,W) and count(l[0],l[1]-1,count_lis) and maze(l[0],l[1]-1,map_lis):
          num_lis[k+1].append([l[0],l[1]-1])
          count_lis[l[0]][l[1]-1] = 1
        if prob(l[0]+1,l[1],H,W) and count(l[0]+1,l[1],count_lis) and maze(l[0]+1,l[1],map_lis):
          num_lis[k+1].append([l[0]+1,l[1]])
          count_lis[l[0]+1][l[1]] = 1
        if prob(l[0],l[1]+1,H,W) and count(l[0],l[1]+1,count_lis) and maze(l[0],l[1]+1,map_lis):
          num_lis[k+1].append([l[0],l[1]+1])
          count_lis[l[0]][l[1]+1] = 1
      new_ans = 0
      for m in num_lis[1:]:
        if m != []:
          new_ans += 1
        if m == []:
          break
      ans = max(ans, new_ans)
      k += 1
      if num_lis[k] == []:
        break
                                     
print(ans)