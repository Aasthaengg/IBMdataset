import itertools

n, k = map(int, input().split())

t = ( n - 1 ) * ( n - 2 ) // 2 - k

if t < 0:
  print( -1 )

else:
  print( n - 1 + t )
  
  for i in range(1, n):
    print(1, i+1)
  
  for j in range(1, n):
    for i in range(1, j): 
      if t == 0:
        break
      print(i+1,j+1)
      t -= 1