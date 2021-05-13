s=input()
o=["R","U","D"]
e=["L","U","D"]
for i in range(len(s)):
  if i%2==0:
    if s[i] in o:
      pass
    else:
      print("No")
      break
  else:
    if s[i] in e:
      pass
    else:
      print("No")
      break
else:
  print("Yes")