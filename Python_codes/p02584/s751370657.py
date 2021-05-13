import math
X,K,D=map(int,input().split(' '))

n=math.ceil(X/D)
m=math.floor(X/D)

n_moveto0=0

if abs(X-n*D) <= abs(X-m*D):
  n_moveto0=abs(n)
  x_min=X-n*D
else: 
  n_moveto0=abs(m)
  x_min=X-m*D


if n_moveto0>=K:
  print(min([abs(X-D*K),abs(X+D*K)]))
else:
  if (K-n_moveto0)%2==0:
    print(abs(x_min))
  else:
    print(min([abs(x_min+D),abs(x_min-D)]))
