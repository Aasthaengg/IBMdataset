N,T=list(map(int, input().split()))
a=10**5
for _ in range(N):
  c,t=list(map(int, input().split()))
  if t<=T:
    a=min(c,a)
if a==10**5:
  print('TLE')
else:
  print(a)