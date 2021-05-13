s = input()
ans = "NO"
if s[:7] == "keyence" or s[-7:] == "keyence": ans = "YES"
else:
  w = "keyence"
  for i in range(len(s)):
    if w[i] == s[i]: continue
    else: break
  if w[i:] == s[-len(w[i:]):]: ans = "YES"
print(ans)