k = int(input())
s = input()
ans = ''

if len(s) <= k:
  print(s)
else:
  for p in range(len(s)):
    if p < k:
      ans += s[p]
    else:
      ans += '...'
      break
  print(ans)