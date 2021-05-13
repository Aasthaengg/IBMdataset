def agc030_a():
  a, b, c = map(int, input().split())
  # a+b+1枚まではcを食べられる (最後の1枚をcにする)
  c_max = min(c, a+b+1)
  ans = b + c_max
  print(ans)

agc030_a()