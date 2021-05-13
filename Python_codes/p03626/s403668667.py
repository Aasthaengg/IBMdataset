n = int(input())
b = []
s1, s2 = input(), input()
now = 0
while now < n:
  if s1[now] == s2[now]:
    b.append(1)
    now += 1
  else:
    b.append(0)
    now += 2
if b[0]:
  ans = 3
else:
  ans = 6
for i in range(len(b)-1):
  if b[i]:
    ans *= 2
  elif not b[i+1]:
    ans *= 3
  ans %= 10**9+7
print(ans)