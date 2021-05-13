N,K=map(int,input().split())

if K%2==1:
  m=N//K
  print(m**3)
else:
  m=(N//K)
  n=(N+K//2)//K
  print(m**3+n**3)