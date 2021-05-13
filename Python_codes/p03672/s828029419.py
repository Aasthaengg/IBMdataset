s = input()
s = s[:-2]
n = len(s)
ans = 0
for i in range(1,n):
  try:
    if s[:i] == s[i:i*2]:
      ans = max(ans, i*2)
  except:
    break
print(ans)