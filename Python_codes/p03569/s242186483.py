s = '0' + input() + '0'
prev = 0
n = len(s)
t = ''
L = []
for i in range(n):
  if s[i] != 'x':
    L.append(i)
    t = t[:] + s[i]
flg = True
n = len(t)
for i in range(n//2):
  flg *= (t[i] == t[n-i-1])
for i in range(n-1):
  L[i] = L[i+1] - L[i] - 1
n -= 1
if flg:
  cnt = 0
  for i in range(n//2):
    cnt += abs(L[i] - L[n-i-1])
  print(cnt)
else:
  print(-1)