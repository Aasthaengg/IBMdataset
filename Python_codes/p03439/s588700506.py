def solve():
  n=int(input())
  l=0
  r=n-1
  print(l,flush=True)
  lt=input()
  if lt=='Vacant':
    return
  print(r,flush=True)
  rt=input()
  if rt=='Vacant':
    return
  while 1:
    center=(l+r)//2
    print(center,flush=True)
    ct=input()
    if ct=='Vacant':
      return
    if (center-l)%2==0:
      if lt!=ct:
        r=center
        rt=ct
      else:
        l=center
        lt=ct
    else:
      if lt==ct:
        r=center
        rt=ct
      else:
        l=center
        lt=ct
solve()