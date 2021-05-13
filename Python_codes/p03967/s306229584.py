s = input()
ans = 0
for i,t in enumerate(s):
  if i&1 == 0 and t == 'p':
    ans -= 1
  elif i&1 == 1 and t == 'g':
    ans += 1
print(ans)
