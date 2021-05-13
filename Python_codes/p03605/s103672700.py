N = list(map(int, input()))
cnt = 0
for i in N:
  if i==9:
    cnt += 1
if cnt==0:
  print('No')
else:
  print('Yes')