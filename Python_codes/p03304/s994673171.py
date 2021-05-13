n, m, d = map(int, input().split())

if d == 0 :
  print('{:.8f}'.format(max(0, (n - d)) * (m - 1) / (n * n)))
else :
  print('{:.8f}'.format(max(0, (n - d)) * 2 * (m - 1) / (n * n)))