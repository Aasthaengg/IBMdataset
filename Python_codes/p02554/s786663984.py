n=int(input())
if n==1:
  print(0)
else:
  zen=10**n
  no=8**n
  zero=zen-9**n
  x=no+2*zero-zen
  print(int(x%(10**9+7)))