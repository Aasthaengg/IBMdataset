#12:17
n = int(input())
a = list(map(int,input().split()))
plus = []
minus = []
for i in range(n):
  if a[i] >= 0:
    plus.append(a[i])
  else:
    minus.append(a[i])
plus.sort()
minus.sort(reverse=True)
lp = len(plus)
lm = len(minus)
if lp >= 1 and lm >= 1:
  ans = sum(plus) - sum(minus)
  print(ans)
  x = minus[0]
  lp = len(plus)
  for i in range(1,lp):
    print(x,plus[i])
    x = x - plus[i]
  minus[0] = x
  x = plus[0]
  for j in range(lm):
    print(x,minus[j])
    x = x - minus[j]
elif lp == 0:
  ans = - sum(minus) + 2 * max(minus)
  print(ans)
  x = minus[1]
  for j in range(2,lm):
    print(x,minus[j])
    x = x - minus[j]
  print(x,minus[0])
elif lm == 0:
  ans = sum(plus) - 2 * min(plus)
  print(ans)
  x = plus[0]
  for i in range(2,lp):
    print(x,plus[i])
    x = x - plus[i]
  print(plus[1],x)