s=list(str(input()))
if len(s)%2!=0:
  print("No")
else:
  for i in range(len(s)):
    if (i%2==0 and s[i]!="h") or (i%2!=0 and s[i]!="i"):
      print("No")
      break
  else:
    print("Yes")