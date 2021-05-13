s = input()
n = len(s) - 1

a = 0
for x in  range(2**n):
  ans = s[0]
  for y in range(n):
    if (x>>y)&1:
      ans = ans + "+" + s[y+1]
    else:
      ans = ans + s[y+1]
  a += eval(ans)
print(a)