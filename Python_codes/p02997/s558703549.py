n,k = map(int,input().split())
mx  = (n-1)*(n-2)//2
li  = []

if k>mx:
  print('-1')
else:
  e = mx-k
  M = (n-1)+e
  print(M)

  for i in range(n-1,0,-1):
    for j in range(1,i):
      li.append([i,j])

  for i in range(1,n):
    print(n,i)
  
  for i in range(e):
    print(*li[i])
