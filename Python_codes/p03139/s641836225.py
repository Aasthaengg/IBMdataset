n,a,b=map(int,input().split())
M=min(a,b)
if a+b<=n:
  m=0
else:
  m=a+b-n
print(M,m)