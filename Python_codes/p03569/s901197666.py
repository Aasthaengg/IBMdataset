s=input()
a=l=0
r=len(s)-1
while l<r:
  if s[l]=="x":
    if s[r]=="x":
      l+=1
      r-=1
    else:
      a+=1
      l+=1
  else:
    if s[r]=="x":
      a+=1
      r-=1
    else:
      if s[l]==s[r]:
        l+=1
        r-=1
      else:
        print(-1)
        exit()
print(a)