s,t,k = map(int,input().split())
n = s
m = t
if k<=s:
  n = n-k
  print(n,m)
elif s+t>=k>s:
  n = 0
  m = s+t-k
  print(n,m)
else:
  print(0,0)