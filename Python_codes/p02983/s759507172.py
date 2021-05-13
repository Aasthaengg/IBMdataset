a,b=map(int,input().split())
mod=2019
if b-a>=2018:
  print('0')
else:
  ans=2018
  for i in range(a,b+1):
    for j in range(i+1,b+1):
      ans=min(ans,(i*j)%mod)
  print(ans)
