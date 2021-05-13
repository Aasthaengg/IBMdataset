def palindrom(i):
  s = str(i)
  return s[0] == s[4] and s[1] == s[3]

a, b = map(int, input().split())
ans = 0
for i in range(a, b + 1):
  if palindrom(i):
    ans += 1
print(ans)
