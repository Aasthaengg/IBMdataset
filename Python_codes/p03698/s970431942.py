s=list(input())
li=[]
non=False
for c in s:
  if c in li:
    non=True
    break
  li.append(c)
    
if non:
  print("no")
  
else:
  print("yes")