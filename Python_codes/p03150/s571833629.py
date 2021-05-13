s = "0"+input()+'0'
l = len(s)-2
for i in range(1,l+1):
  for j in range(i,l+1):
    a = s[:i]+s[j:]
    if a=="0keyence0":
      print("YES")
      exit()
print("NO")