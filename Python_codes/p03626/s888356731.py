n = int(input())
s1 = input()
s2 = input()
mod = 10 ** 9 + 7
if s1[0] == s2[0]:
  ans = 3
  flag = 1
  now = 1
else:
  ans = 6
  flag = 0
  now = 2
while now < n:
  if s1[now] == s2[now]:
    if flag:
      ans *= 2
    flag = 1
    now += 1
  else:
    if flag:
      ans *= 2
    else:
      ans *= 3
    flag = 0
    now += 2
  ans %= mod
print(ans)