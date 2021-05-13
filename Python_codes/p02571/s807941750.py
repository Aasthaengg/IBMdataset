s = input()
t = input()
ans = 10**10
l = len(s) - len(t) + 1
for i in range(l):
  tans = 0
  for j in range(len(t)):
    if s[i+j] != t[j]:
      tans += 1
  ans = min(ans, tans)
print(ans)