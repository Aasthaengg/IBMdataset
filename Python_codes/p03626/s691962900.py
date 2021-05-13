n = int(input())
s1 = input()
s2 = input()
mod = 10**9+7
if s1[0]==s2[0]:
  ans = 3
  pre = '-'
  i = 1
else:
  ans = 6
  pre = '|'
  i = 2
while i<n:
  if s1[i]==s2[i]:
    if pre=='-':
      ans *= 2
      ans %= mod
    pre = '-'
    i += 1
  else:
    if pre=='-':
      ans *= 2
      ans %= mod
    else:
      ans *= 3
      ans %= mod
    pre = '|'
    i += 2
print(ans)