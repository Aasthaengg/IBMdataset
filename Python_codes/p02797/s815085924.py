n,k,s=map(int,input().split())
for i in range(k):
  print(s)
for i in range(n-k):
  if s==10**9:
    print(s-1)
  else:
    print(s+1)