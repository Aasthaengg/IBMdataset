l,r=map(int,input().split())

sho_l = l // 2019
sho_r = r // 2019

if sho_r-sho_l >= 1:
  print(0)
else:
  ans = 2018
  for i in range(l,r):
    for j in range(i+1,r+1):
      ans = min((i*j)%2019,ans)
  print(ans)
