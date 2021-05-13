N = int(input())

if N%2 == 0:
  print(N, N, N//2)
else:
  for h in range(3500, -1, -1):
    num = N*h*h; diff_num = N*h
    dem = 4*h*h - N*(h+h); diff_dem = 4*h - N
    for n in range(h, -1, -1):
      if dem <= 0:
        break
      if num%dem == 0:
        print(h, n, num//dem)
        quit()
      num -= diff_num
      dem -= diff_dem