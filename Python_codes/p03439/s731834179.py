n=int(input())
l=0
center=(n-1)//2
r=n-1
print(center,flush=True)
ct=input()
if ct=='Vacant':
  exit()
print(l,flush=True)
lt=input()
if lt=='Vacant':
  exit()
print(r,flush=True)
rt=input()
if rt=='Vacant':
  exit()
flag=False
if (center-l)%2==0:
  if lt!=ct:
    r=center
    rt=ct
    flag=True
else:
  if lt==ct:
    r=center
    rt=ct
    flag=True
if flag==False:
  if (r-center)%2==0:
    if rt!=ct:
      l=center
      lt=ct
  else:
    if rt==ct:
      l=center
      lt=ct
while 1:
  center=(l+r)//2
  print(center,flush=True)
  ct=input()
  if ct=='Vacant':
    exit()
  flag=False
  if (center-l)%2==0:
    if lt!=ct:
      r=center
      rt=ct
      flag=True
  else:
    if lt==ct:
      r=center
      rt=ct
      flag=True
  if flag==False:
    if (r-center)%2==0:
      if rt!=ct:
        l=center
        lt=ct
    else:
      if rt==ct:
        l=center
        lt=ct