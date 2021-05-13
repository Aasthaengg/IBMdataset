n,k = map(int,input().split())

if k == 1:
   print(0)
else:
   g = n - (k - 1)
   if g == 1:
      print(0)
   elif g < 1:
      print(1)
   else:
      print(g-1)