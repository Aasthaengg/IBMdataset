x=int(input())
if x<=6:
  print(1)
else:
  ans=(x//11)*2
  if x%11==0:
     pass 
  elif (x//11)%2==0:
    if x%11<=6:
      ans+=1
    else:
      ans+=2
  else:
    if x%11<=5:
      ans+=1
    else:
      ans+=2
  print(ans)