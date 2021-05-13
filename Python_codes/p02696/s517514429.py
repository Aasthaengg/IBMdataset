A,B,N = map(int,input().split())
def f(x):
  f = int((A*x)/B)-A*int(x/B)
  return f
if(B-1 < N):
  print(f(B-1))
else:
  print(f(N))