a,b,k = map(int,input().split())
ak = a+k
bk = b-k

if a+k>=b:
  for i in range(a,b+1):
    if i<ak or i>bk:
      print(i)
else:
  for i in range(a,a+k+1):
    if i<ak or i>bk:
      print(i)
  if i<b-k:
    for n in range(b-k,b+1):
      if n<b-k or n>bk:
        print(n)
  else:
    for j in range(i+1,b+1):
      if j<ak or j>bk:
        print(j)