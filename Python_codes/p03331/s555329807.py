n = input()
n_ = n.replace('0','')
if n_ == '1':
  print(10)
else:
  a = 0
  for s in n:
    a += int(s)
  print(a)