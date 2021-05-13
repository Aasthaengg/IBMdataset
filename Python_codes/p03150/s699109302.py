s = input()
for i in range(8):
  temp = s[:i] + s[-7 + i:]
  if temp == "keyence":
    print("YES")
    break
else:
  print("NO")