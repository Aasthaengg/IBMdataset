n,m,d = map(int,input().split())
if d == 0:
  print((m-1)/n)
else:
  a = 2*(n-d)-(2*d-n>=0)*(2*d-n)*2
  print(a*(m-1)/pow(n,2))