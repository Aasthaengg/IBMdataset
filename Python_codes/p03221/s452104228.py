n,m = map(int,input().split())
l = []
s = ""
tmp = 1
for i in range(m):
  p,y = map(int,input().split())
  l.append([str(p).zfill(6),y,i+1])
  
l = sorted(l, key=lambda x:(x[0],x[1]))
#print(l)
for i in range(m):
  s = ""
  if i == 0 or l[i-1][0] != l[i][0]:
    tmp = 1
  else:
    tmp += 1
  s = l[i][0] + str(tmp).zfill(6)
  l[i].append(s)
    
l = sorted(l, key=lambda x:(x[2]))

for i in range(m):
  print(l[i][3])