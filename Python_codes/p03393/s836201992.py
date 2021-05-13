s = str(input())
ans = ''
if len(s) < 26:
  for i in range(ord('a'), ord('z')+1):
    if chr(i) not in s:
      ans = s + chr(i)
      break
else:
  for i in range(24, -1, -1):
    if ord(s[i]) < ord(s[i+1]):
      ans = s[:i]
      for j in range(ord(s[i])+1, ord('z')+1):
        if chr(j) not in ans:
          ans += chr(j)
          break
      break
if ans: print(ans)
else: print(-1)