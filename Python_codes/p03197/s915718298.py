n=int(input())
a=[int(input()) for _ in range(n)]
flg=False
for x in a:
  if x%2==1:
    flg=True
if flg:
  print('first')
else:
  print('second')