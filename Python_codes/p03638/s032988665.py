H,W = map(int,input().split())
N = int(input())
A = []
for i, a in enumerate(map(int,input().split())):
  A.append([a,i+1])
A.sort(reverse= True)
grids = [[-1 for _ in range(W)] for _ in range(H)]

pos = [0,0]
for a,i in A:
  cnt = 0
  while cnt != a:
    grids[pos[1]][pos[0]] = i
    cnt += 1
    if pos[1]%2==0:
      if pos[0] != W-1: pos[0] +=1
      else: pos = [W-1,pos[1]+1]
    else:
      if pos[0] != 0: pos[0] -=1
      else: pos = [0,pos[1]+1]

[print(*row) for row in grids]