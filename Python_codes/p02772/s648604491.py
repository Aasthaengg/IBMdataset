n = int(input())
a = list(map(int,input().split()))
ans = True
for i in a:
  if i % 2 == 0:
    if not (i % 3 == 0 or i % 5 == 0):
      ans = False
      break
if ans:
  print('APPROVED')
else:
  print('DENIED')
