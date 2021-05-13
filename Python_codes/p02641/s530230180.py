x,n=[int(x) for x in input().split()]
if n==0:
  print(x)
else:
  p=[int(x) for x in input().split()]
  ans=[]
  Flag=False
  while ans==[]:
    for i in range(105):
      if x-i not in p:
        ans.append(x-i)
        Flag=True
        break
      elif x+i not in p:
        ans.append(x+i)
        Flag=True
        break
    if Flag:
      break
  print(min(ans))