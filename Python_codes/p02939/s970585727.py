s = input()
n = len(s)

bef = s[0]
key = 0
ans = 1
for i in range(1, n):
  if key == i:
    continue
  if bef == s[i]:
    if i == n-1:
      continue
    bef = s[i:i+2]
    ans += 1
    key = i+1
  else:
    bef = s[i]
    ans += 1
print(ans)