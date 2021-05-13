s = input()

s = list(s)
s1 = s[0:len(s)//2]
s2 = s[len(s)//2+1:len(s)]
if ("".join(s1) == "".join(s2)) :
  print("Yes")
else :    
  print("No")