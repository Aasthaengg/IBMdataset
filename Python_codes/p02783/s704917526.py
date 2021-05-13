h,a = list(map(int,input().split()))

if h % a >= 1:
  print(h // a + 1)
else:
  print(h // a)