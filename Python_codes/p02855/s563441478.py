h,w,k = map(int,input().split())
F = [input() for _ in range(h)]
A = [[0]*w for _ in range(h)]

def square(F,A,y,x,h,w,color):
  r,l,u,d = 0,0,0,0
  
  while x+r+1 < w:      
    if F[y][x+r+1] == '.' and A[y][x+r+1] == 0:
      r += 1
    else:
      break
      
  while x-l-1 >= 0:      
    if F[y][x-l-1] == '.' and A[y][x-l-1] == 0:
      l += 1
    else:
      break     
      
  while y-u-1 >= 0:
    tmp = 0
    
    for i in range(-l,r+1):            
      tmp += (F[y-u-1][x+i] == '.' and A[y-u-1][x+i] == 0)    
    if tmp == r + l + 1:
      u += 1
    else:
      break
    
  while y+d+1 < h:
    tmp = 0
    for i in range(-l,r+1):  
      tmp += (F[y+d+1][x+i] == '.' and A[y+d+1][x+i] == 0)
    if tmp == r + l + 1:
      d += 1
    else:
      break
    
  for i in range(y-u,y+d+1):
    for j in range(x-l,x+r+1):
      A[i][j] = color  
      
c = 1
for i in range(h):
  for j in range(w):    
    if A[i][j] != 0:
      continue
    if F[i][j] == '#':
      square(F,A,i,j,h,w,c)
      c += 1
      
for i in range(h):
  print(*A[i])      