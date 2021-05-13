n,k=[int(x) for x in input().split()]
h=[int(x) for x in input().split()]
h.sort()
H=h[:(n-k)]
if n<=k:
  print(0)
else:
  print(sum(H))