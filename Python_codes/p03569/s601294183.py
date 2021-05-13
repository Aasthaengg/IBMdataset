s = input()
l, r=0, len(s)-1
ret = 0
while l<r:
  L, R=s[l], s[r]
  if L==R:
    l+=1
    r-=1
  elif L=='x':
    l+=1
    ret+=1
  elif R=='x':
    r-=1
    ret+=1
  else:
    ret=-1
    break
print(ret)