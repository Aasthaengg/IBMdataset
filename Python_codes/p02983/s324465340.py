l,r = map(int,input().split())
if r-l>=2018:
  print(0)
else:
  ans = float('inf')
  for i in range(r-l):
    for j in range(i+1,r-l+1):
      ans = min((((l+i)%2019)*((l+j)%2019))%2019,ans)
  print(ans)