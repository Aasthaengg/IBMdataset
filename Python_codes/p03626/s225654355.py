n = int(input())
s = input()
t = input()

ans = 1
mod = 10**9+7
bef = True
skip = -1
for i in range(n):
  if skip == i:
      continue
  if i == 0:
    if s[i] == t[i]:
      ans *= 3
    else:
      ans *= 6
  elif bef:
    ans *= 2
  else:
    if s[i] != t[i]:
      ans *= 3
  if s[i] == t[i]:
    bef = True
  else:
    bef = False
    skip = i+1
  ans %= mod
print(ans)