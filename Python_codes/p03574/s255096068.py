def bakudanda (y,x):
  if y < 0 or y >= len(s):
    return 0
  if x < 0 or x >= len(s[y]):
    return 0
  if s[y][x] == '#':
    return 1
  else:
    return 0
H,W = map(int,input().split())
s=[]
for i in range(H):
  s.append(input())
  
for i in range(len(s)):
  a = s[i]
  fp = ''
  for j in range(len(a)):
    if a[j] == '.':
      c = 0
      ds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0,1), (1, -1), (1, 0), (1, 1)]
      for (y, x) in ds:
        c+= bakudanda(i+y,j+x)
      fp += str(c)
    else:
      fp += '#'
  print(fp)
        
