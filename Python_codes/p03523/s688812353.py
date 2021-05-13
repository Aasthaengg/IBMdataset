s=input()
a=[]
for i in range(1<<4):
  l=list("AKIHABARA")
  for j in range(len(l)):
    if i&(1<<j):
      if j==0:
        l[0]=""
      elif j==1:
        l[4]=""
      elif j==2:
        l[6]=""
      elif j==3:
        l[8]=""
  a.append("".join(l))
if s in a:
  print("YES")
else:
  print("NO")