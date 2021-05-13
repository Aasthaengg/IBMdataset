s=input()
a=["dreamer", "dream", "eraser", "erase"]
while s:
  for i in a:
    k=len(i)
    if s[-k:]==i:
      s=s[:-k]
      break
  else:
  	break

if s=="":
  print("YES")
else:
  print("NO")