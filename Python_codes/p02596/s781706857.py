b = 0
K = int(input())
a = 7 % K
for i in range(K):
  if a == 0:
    b = 1
    break
  else:
    a = (10 * a +7) % K
if b == 0:
  print(-1)
else:
  print(i + 1)