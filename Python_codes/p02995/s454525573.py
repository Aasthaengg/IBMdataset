import math
a, b, c, d=map(int, input().split())
#aとbの間の cの倍数の数
if a%c==0:
  abc=b//c-a//c+1
else:
  abc=b//c-a//c  
  
#aとbの間の dの倍数の数
if a%d==0:
  abd=b//d-a//d+1
else:
  abd=b//d-a//d
#aとbの間の cdの倍数の数
e=(c*d)//math.gcd(c, d)
if a%e==0:
  abcd=b//e-a//e+1
else:
  abcd=b//e-a//e

print(b-a+1-(abc+abd-abcd))
