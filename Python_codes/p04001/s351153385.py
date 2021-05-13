s = input()
n = len(s)
ans = 0
for i in range(2**(n-1)):
  flag = [False] * (n-1)
  for j in range(n-1):
    if (i >> j) & 1:
      flag[j] = True
  tmp = int(s[0])
  for k in range(n-1):
    if flag[k]:
      ans += tmp
      tmp = int(s[k+1])
    else:
      tmp *= 10
      tmp += int(s[k+1])
  ans += tmp
print(ans)