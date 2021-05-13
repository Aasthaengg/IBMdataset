x,k,d=map(int,input().split())
if x>=0:
  if x//d>=k:
    print(abs(x-k*d))
  else:
    if (k-(x//d))%2==0:
      print(abs(x-(x//d)*d))
    else:
      print(abs(x-(x//d)*d-d))
else:
  if -x//d>=k:
    print(abs(x+k*d))
  else:
    if (k-(-x//d))%2==0:
      print(abs(x+(-x//d)*d))
    else:
      print(abs(x+(-x//d)*d+d))