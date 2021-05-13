S=list(str(input()))
zero=S.count("0")
one=S.count("1")
if zero==0 or one==0:
  print(0)
else:
  print(min(zero,one)*2)