L,R = list(map(int,input().split()))

if R - L >= 2018:
  print(0)
else:
  min_mod = 2019
  for i in range(L,R+1):
    for j in range(i+1,R+1):
      tmp = (i * j) % 2019
      if tmp < min_mod:
        min_mod = tmp
  print(min_mod)