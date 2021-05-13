a,b,c = map(int,input().split())
if a == b and b == c and a == c:
  if a %2 == 0:
    print(-1)
  else:
    print(0)
else:
  for i in range(10**9):
    if a %2 == 0:
      S = a/2
    else:
      print(i)
      break
    if b%2 == 0:
      T = b/2
    else:
      print(i)
      break
    if c %2 == 0:
      U = c/2
    else:
      print(i)
      break
    a -= S*2
    b -= T*2
    c -= U*2
    a += T
    a += U
    b += S
    b += U
    c += S
    c += T