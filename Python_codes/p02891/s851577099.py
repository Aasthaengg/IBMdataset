s = input()
k = int(input())
ans = 0
s2 = s[0]
for i in range(len(s) - 1):
  if s2[i] == s[i + 1]:
    s2 += '9'
    ans += 1
  else:
    s2 += s[i + 1]
ans = ans * k 
if s2[0] == s2[-1] and len(s) >= 2:
  m = 0
  for i in range(len(s)):
    if s[i] == s2[-1]:
      m += 1
    else:
      break
  if m % 2 == 1:
    ans += k - 1
if len(s) == 1:
  ans = k // 2
if len(list(set(list(s)))) == 1:
  ans = len(s) * k // 2
print(ans)