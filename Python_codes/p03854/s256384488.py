s = input()[::-1]
a = "maerd"
b = "remaerd"
c = "esare"
d = "resare"
while len(s)!=0:
  if s[:5]==a:
    s = s[5:]
  elif s[:7]==b:
    s = s[7:]
  elif s[:5]==c:
    s = s[5:]
  elif s[:6]==d:
    s = s[6:]
  else:
    print("NO")
    exit()
print("YES")