N,K=map(int, input().split())
if K<0:
  print('NO')
else:
  print('YES' if N>=2*K-1 else 'NO')