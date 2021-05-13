X=int(input())

if X >= 2000:
  print("1")
else:
  p=X//100
  if 100*p <= X <= 105*p:
    print("1")
  else:
    print("0")