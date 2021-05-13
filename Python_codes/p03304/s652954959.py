n,m,d = map(int,input().split())
if d == 0 :
  print('{:.10f}'.format((m-1)/n))
else :
  print('{:.10f}'.format((m-1)*2.0*(n-d)/(n*n)))
