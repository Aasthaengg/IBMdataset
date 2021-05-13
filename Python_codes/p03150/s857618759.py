s = input()
b = s[:7]
e = s[-7:]
flg = 0
for i in range(7):
  if b[:i] + e[i:] == "keyence":
    flg = 1
if flg:
  print("YES")
else:
  print("NO")