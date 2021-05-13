h, w, k = map(int,input().split())
c = []
for i in range(h):
  c.append(input())
  
def countb(c):
  num = 0
  for i in range(h):
    num += c[i].count("#")
  return(num)

def printb(c, row, col):
  c = c[:]
  #print(row,col)
  cnt = 0
  while row != 0:
    if row  & 0b1:
     
      c[cnt] = "."*w
    cnt += 1
    row = row >> 1
  
  cnt = 0
  while col != 0:
    #print(col&0b1)
    if col & 0b1:
      for i in range(h):
        c[i] = c[i][:cnt]+"."+c[i][cnt+1:]
    cnt += 1
    col = col >> 1
    
  #print("\n".join(c))
  return countb(c)

ans = 0
for i in range(2**h):
  for j in range(2**w):
    if printb(c,i,j) == k:
      ans += 1
print(ans)
