s=str(input())
t=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
if len(s)!=26:
  s=list(s)
  for i in range(26):
    if t[i] not in s:
      s.append(t[i])
      break
  print("".join(s))
else:
  if "".join(s)=="zyxwvutsrqponmlkjihgfedcba":
    print(-1)
  else:
    a=[]
    for i in range(26):
      a.append(s[25-i])
      for j in a:
        if s<s[:25-i]+j:
          print(s[:25-i]+j)
          exit()