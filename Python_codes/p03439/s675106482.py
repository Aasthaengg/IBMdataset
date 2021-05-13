def printf(i):
  print(i,flush=True)
n=int(input())
printf(0)
ls=input()
if ls=='Vacant':
  exit()
l=0
r=n
while True:
  m=(l+r)//2
  printf(m)
  ch=input()
  if ch=='Vacant':
    exit()
  if ls==ch:
    if (m-l)%2:
      r=m
    else:
      l=m
  else:
    if (m-l)%2:
      l=m
      ls=ch
    else:
      r=m