N,K = map(int, input().split())
A = list(map(int, input().split())) 
A.sort()
A.reverse() 
x = A[0]   
for i in range (1, N):
  while A[i] != 0:
    x , A[i] = A[i] , x % A[i]
if K > A[0]:
  print('IMPOSSIBLE')
else:
  print('POSSIBLE' if K%x == 0 else 'IMPOSSIBLE')