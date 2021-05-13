a,b=map(int,input().split())
s=[]
g=[['#']*100 for i in range(100)]
for i in range(1,100,4):
  for j in range(1,100,4):
    s.append((i,j))
if a>=b:
  for i in range(a):
    y,x=s[i]
    for dy in [-1,0,1]:
      for dx in [-1,0,1]:
        if dy==dx==0:
          continue
        g[y+dy][x+dx]='.'
  for i in range(a-b+1):
    y,x=s[i]
    g[y][x]='.'
else:
  for i in range(100):
    for j in range(100):
      g[i][j]='.'
  for i in range(b):
    y,x=s[i]
    for dy in [-1,0,1]:
      for dx in [-1,0,1]:
        if dy==dx==0:
          continue
        g[y+dy][x+dx]='#'
  for i in range(b-a+1):
    y,x=s[i]
    g[y][x]='#'
print(100,100)
for i in range(100):
  print(''.join(g[i]))