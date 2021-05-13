N=int(input())
a=[int(input()) for _ in range(N)]

flag=1
for i in range(N):
  if a[i]%2:
    flag=0
    break
    
if flag:
  print('second')
else:
  print('first')