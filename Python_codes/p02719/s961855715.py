n,k=map(int,input().split())

if n%k==0:
  print(0)
elif n<=k:
  print(min(n,k-n))
else:
  num=n%k
  print(k-num)

