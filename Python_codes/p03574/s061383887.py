h, w = [int(x) for x in input().split()]
s = []
s.append(list("･" * (w + 2)))
for _ in range(h):
  s.append(list("･" + input() + "･"))
  
s.append(list("･" * (w + 2)))

for i in range(1, h+1):
  for j in range(1, w+1):
    if s[i][j] == "#":
      continue
    
    neighbors = [
      s[i-1][j-1], 
      s[i-1][j], 
      s[i-1][j+1], 
      s[i][j-1], 
      s[i][j+1], 
      s[i+1][j-1], 
      s[i+1][j], 
      s[i+1][j+1],
    ]
    s[i][j] = str(len(list(filter(lambda x : x == "#", neighbors))))

for l in s[1:len(s)-1]:
  print(''.join(l[1:len(l)-1]))
  
