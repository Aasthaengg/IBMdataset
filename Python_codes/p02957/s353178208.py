A, B = map(int, input().split())
K = (A + B) // 2
if abs(K - A) != abs(K - B):
  print('IMPOSSIBLE')
else:
  print(K)