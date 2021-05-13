a,b=map(int,input().split())
k=32
m=2*k
grid=[['#' for i in range(m)] for i in range(k)]
grid=grid+[['.' for i in range(m)] for i in range(k)]

for i in range(m*k):
  if a==1:
    break
  grid[2*int(i*2/m)][(i*2)%m]='.'
  a-=1

for i in range(m*k):
  if b==1:
    break
  grid[k+1+2*int(i*2/m)][(i*2)%m]='#'
  b-=1

print(str(2*k)+' '+str(2*k))
for i in range(k*2):
  print(''.join(grid[i]))