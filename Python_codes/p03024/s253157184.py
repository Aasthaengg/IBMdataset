n = input()
ans = 0
for i in range (len(n)):
  if n[i] == 'o':
    ans += 1
if 15 - len(n) + ans >= 8:
  print("YES")
else:
  print("NO")