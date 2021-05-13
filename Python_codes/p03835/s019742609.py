k,s=map(int,input().split())
 
c=0
m=min(s,k)
for x in range(m+1):
  for y in range(m+1):
    if s<x+y:
      break
    elif s>x+y+k:
      continue
    else:
      c+=1
print(c)