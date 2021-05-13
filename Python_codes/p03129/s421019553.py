N,K = map (int, input ().split ())
if N%2 == 0:
  x = N/2
else:
  x = N//2+1
if K > x:
  print ('NO')
else:
  print ('YES')