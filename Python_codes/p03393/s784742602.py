s = input()
text = 'abcdefghijklmnopqrstuvwxyz'
if len(s) < 26:
  for c in text:
    if c not in s:
      print(s + c)
      break
else:
  cand = {s[-1]}
  for i in range(1, len(s)):
    j = len(s) - i - 1
    if max(cand) > s[j]:
      print(s[:j] + min(c for c in cand if c > s[j]))
      break
    cand.add(s[j])
  else:
    print(-1)