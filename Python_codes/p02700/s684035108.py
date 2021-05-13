a,b,c,d = map(int, input().split())
if a%d ==0:
  ao = a/d
else:
  ao = int(a/d +1)
if c%b ==0:
  taka = c/b
else:
  taka = int(c/b +1)

if taka> ao:
  print('No')
else:
  print('Yes')