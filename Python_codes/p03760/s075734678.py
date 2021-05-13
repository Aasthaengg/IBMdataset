a = input()
b = input()
ans = ''
if len(a) == len(b):
  for i in range(len(a)):
    ans = ans + (a[i]+b[i])
else:
  for i in range(len(a)-1):
    ans = ans +(a[i]+b[i])
  ans = ans + (a[-1])
print(ans)