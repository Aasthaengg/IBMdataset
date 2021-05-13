n, m, d = map(float, input().split())
if (d != 0):
  print('{:.10f}'.format((2 * (n -d) * (m - 1)) / (n * n))) 
else:
  print('{:.10f}'.format(((n -d) * (m - 1)) / (n * n))) 