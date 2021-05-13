check=[list(input()) for i in range(3)]
cur=0
while True:
  if cur==0:
    if len(check[0])==0:
      break
  elif cur==1:
    if len(check[1])==0:
      break
  else:
    if len(check[2])==0:
      break
  cur=ord(check[cur].pop(0))-ord("a")
if cur==0:
  print("A")
elif cur==1:
  print("B")
else:
  print("C")
