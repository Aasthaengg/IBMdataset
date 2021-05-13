s = str(input()); n = len(s)
kn = 7
if n < kn:
  print("NO")
  exit()
for i in range(kn):
  temp = s[:i] + s[n-kn+i:]
  if temp == "keyence":
    print("YES")
    exit()
print("NO")