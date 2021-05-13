N = int(input())
s = list(input())
t = 0
for i in range(N):
  if s[i] == 'R':
    t += 1
  else:
    t -= 1
if t > 0:
  print('Yes')
else:
  print('No')