cnt = 0
def f(n,r,d):
  global cnt
  n = r*n-d
  print(n)
  cnt += 1
  if cnt < 10:
  	f(n,r,d)
r,d,x = map(int,input().split())
f(x,r,d)