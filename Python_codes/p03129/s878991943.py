N,K = map(int,input().split())
if N//2 + (N%2 != 0) >= K:
  print('YES')
else:
  print('NO')