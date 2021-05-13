l,r = map(int,input().split())

mod = 2019

lm = l % mod
rm = r % mod

ans = []
if r - l >= mod :
  print(0)
  exit()
else:
  for i in range(lm,rm):
    for j in range(i+1,rm+1):
      ans.append(i*j % mod)
  print(min(ans))