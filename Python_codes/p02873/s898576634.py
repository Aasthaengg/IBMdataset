S = input()
f = 0
x = 0
y = 0
Y = []
for i in range(len(S)):
  if S[i] == ">":
    if f == 1:
      y += 1
    elif f == 0:
      x = y
      y = 1
      f = 1
  else:
    if f == 0:
      y += 1
    else:
      Y.append([x, y])
      x = 0
      y = 1
      f = 0
if f == 0:
  Y.append([y, 0])
else:
  Y.append([x, y])
      
ans = 0
for y in Y:
  M = max(y)
  m = min(y)
  ans += (M * (M+1) // 2 + m * (m-1) // 2)
print(ans)