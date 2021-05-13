x, k, d = map(int,input().split())
x =abs(x)
s = x//d
if x-k*d>0:
  print(x-k*d)
else:
    if (k-s)%2==0:
        print(x-s*d)
    else:
        print(-x+(s+1)*d)
