n,l = map(int,input().split())
if l > 0:
  print(sum(range(l,l+n))-l)
elif l+n-1<0:
  print(sum(range(l,l+n))-(l+n-1))
else:
  print(sum(range(l,l+n)))