s = list(input())
l = len(s)
t = s[::-1]
 
if s == t and (s[:(l-1)//2] == t[(l+1)//2:]) and (s[(l+1)//2:] == t[:(l-1)//2]):
  print("Yes")
else:
  print("No")
