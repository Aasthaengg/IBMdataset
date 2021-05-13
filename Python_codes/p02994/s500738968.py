N, L = map(int, input().split())
#L, L+N-1 => sum: (2L+N-1)*N // 2
A = (2 * L + N - 1)*N // 2
if L*(L+N-1) <= 0:
  print( A )
elif L+N-1 < 0:
  print( A - (L+N-1) )
else:
  print( A - L )
