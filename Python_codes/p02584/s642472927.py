x,K,D = list(map(int, input().split()))

if x < 0 :
  x = -x

l = x // D

if K > l:
  K = K - l
  if (K % 2) == 0:
    print(abs(x-D*l))
  else:
    print(abs(x-D*(l+1)))
else:
  print(abs(x - D*K))
