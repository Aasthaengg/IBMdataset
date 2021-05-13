n,m,x,y=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
if y-x>=1:
  kouho=[]
  for k in range(x+1,y+1):
    kouho.append(k)
  p.sort()
  q.sort()
  c=0
  for i in range(0,len(kouho)):
    c+=1
    if p[-1]<kouho[i]<=q[0]:
      print("No War")
      break
    if c==len(kouho):
      print("War")
else:
  print("War")