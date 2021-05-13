N , Y = map(int,input().split())
k = 0
for i in range(N+1):
  x = i
  for j in range(N - i + 1):
    y = j
    if (Y - x * 10000 - y*5000)/1000 == N - x - y >=0 :
      print(str(x) +' '+str(y)+' '+str(N-x-y))
      k = 1
      break
  if k == 1:
    break
if k== 0:
  print('-1 -1 -1')