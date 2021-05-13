s = input()
n = len(s) -1
ans = 0
for i in range(2**n):
  e = s[0]
  for j in range(n):
    if i >> j & 1:
      e +='+'
    e += s[j+1]
  ans += eval(e)
print(ans)
