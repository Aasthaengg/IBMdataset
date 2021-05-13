S = input()
x = len(S)
y = 15 - x
z = ""
point = 0
for i in range(x):
  z = S[i]
  if (z == "o"):
    point += 1
  else:
    point += 0
    
y = y + point
if (y >= 8):
  print("YES")
else:
  print("NO")