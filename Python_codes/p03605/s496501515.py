n = input()
ans = 0
for i in n:
  if i=='9':
    ans += 1
if ans > 0:
  print("Yes")
else:
  print("No")