s = input()
ans = 0
gcount = 0

for i in range(len(s)):
  if s[i] == 'g':
    if gcount > 0:
      ans += 1
      gcount -= 1
    else:
      gcount += 1
    
  else:
    if gcount > 0:
      gcount -= 1
    else:
      ans -= 1
      gcount += 1
print(ans)
