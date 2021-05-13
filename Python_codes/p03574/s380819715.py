h, w = map(int, input().split())

sn = [input() for _ in range(h)]
csn = [[0] * w for i in range(h)]

for i in range(h):
  for j in range(w):
    if sn[i][j] == "#" :
      csn[i][j] = -1
      if i-1 >= 0 and sn[i-1][j] == "." :
        csn[i-1][j] += 1
        
      if i+1 <= h-1 and sn[i+1][j] == "." :
        csn[i+1][j] += 1   
        
      if j-1 >= 0 and sn[i][j-1] == "." :
        csn[i][j-1] += 1
        
      if j+1 <= w-1 and sn[i][j+1] == "." :
        csn[i][j+1] += 1        

      if i-1 >= 0 and j-1 >= 0 and sn[i-1][j-1] == "." :
        csn[i-1][j-1] += 1
 
      if i-1 >= 0 and j+1 <= w-1  and sn[i-1][j+1] == "." :
        csn[i-1][j+1] += 1 

      if i+1 <= h-1 and j-1 >= 0 and sn[i+1][j-1] == "." :
        csn[i+1][j-1] += 1        
        
      if i+1 <= h-1 and j+1 <= w-1 and sn[i+1][j+1] == "." :
        csn[i+1][j+1] += 1    
        
for i in range(h):
  for j in range(w):  
    if csn[i][j] == -1 :
      print("#", end='')
    else :
      print(csn[i][j], end='')
  print()