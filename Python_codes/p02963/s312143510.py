s = int(input())
if s <= 10**9:
  print(0,0,s,1,0,1)
elif s == 10**18:
  print(0,0,10**9,0,0,10**9)
else:
  m = s//10**9+1
  a = 10**9-s%10**9
  print(0,0,m,1,a,10**9)