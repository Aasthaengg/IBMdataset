mod = 1000000007
n = int(input())
s = input()
l = []
for i in range(1, n):
  if s[i - 1] == s[i]:
    l.append(2)
  elif i < 2 or s[i - 2] != s[i - 1]:
    l.append(1)
if n < 2 or s[n - 2] != s[n - 1]:
  l.append(1)
if l[0] == 1:
  ans = 3
else:
  ans = 6
for i in range(1, len(l)):
  if l[i - 1] == 1:
    ans = 2 * ans % mod
  elif l[i] == 2:
    ans = 3 * ans % mod
print(ans)
