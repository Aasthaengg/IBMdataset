n,m=map(int,input().split())
MOD=10**9+7
ans = 1
if abs(n-m) > 1:
  print(0)
  exit()
else:
  if abs(n-m) == 0:
    for i in range(1,n+1):
      ans = ans*i%MOD
    for i in range(1,m+1):
      ans = ans*i%MOD
    ans = ans*2%MOD
  else:
    for i in range(1,n+1):
      ans = ans*i%MOD
    for i in range(1,m+1):
      ans = ans*i%MOD
print(ans)
    
