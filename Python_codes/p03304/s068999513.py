n,m,d = map(int, raw_input().split())
if d == 0:
  print float(m-1) / float(n)
else:
  print float((m-1)*2*(n-d)) / float(n**2)
