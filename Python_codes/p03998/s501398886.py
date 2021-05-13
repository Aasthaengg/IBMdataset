check=[list(input()) for i in range(3)]
cur=0
flag=True
while flag:
  if (len(check[0])==0 and cur==0) or (len(check[1])==0 and cur==1) or (len(check[2])==0 and cur==2):
    flag=False
    break
  temp=check[cur].pop(0)
  if temp=="a":
    cur=0
  elif temp=="b":
    cur=1
  else:
    cur=2
if cur==0:
  print("A")
elif cur==1:
  print("B")
else:
  print("C")
