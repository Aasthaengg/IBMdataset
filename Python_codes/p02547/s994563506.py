N = int(input())
count = 0
for i in range(N):
  n,m = input().split(' ')
  if n == m :
    count += 1
    if count >= 3:
      break
  else:
    count = 0
if count >= 3:
  print('Yes')
else :
  print('No')