n = int(input())
x = input()
one = x.count("1")
base1 = 0
base2 = 0
if one == 1:
  idx = n - x.index("1") - 1
  base = pow(2,idx,2)
  for k,v in enumerate(x):
    now = base
    if v == "0":
      now += pow(2,n-k-1,2)
      if now % 2:
        print(2)
      else:
        print(1)
    else:
      print(0)
  exit()
for k,v in enumerate(x[::-1]):
  if v == "1":
    base1 += pow(2,k,one+1)
    base2 += pow(2,k,one-1)
base1 %= one+1
base2 %= one-1

for k,v in enumerate(x):
  ans = 1
  if v == "0":
    now = base1 + pow(2,n-k-1,one+1)
    now %= one+1
  else:
    now = base2 - pow(2,n-k-1,one-1)
    now %= one-1
  while now > 0:
    popcount = bin(now).count("1")
    now %= popcount
    ans += 1
  print(ans)