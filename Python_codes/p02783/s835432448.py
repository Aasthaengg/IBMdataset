h,a = map(int, input().split())
if h <= a:
  print(1)
else:
  if h%a == 0:
    print(h//a)
  else:
    print(h//a + 1)