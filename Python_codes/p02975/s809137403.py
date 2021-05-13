n=int(input())
a=sorted(list(map(int,input().split())))
if n%3==0:
  d={}
  for ai in a:
    if ai not in d:
      d[ai]=a.count(ai)
      if len(d)==4:
        break
  sa=list(set(a))
  if len(sa)==3 and sa[0]^sa[1]==sa[2] and d[sa[0]]==d[sa[1]] and d[sa[0]]==d[sa[2]]:
    print('Yes')
    exit()
  if len(sa)==2 and 0 in d and 2*d[0]==max(d[sa[0]],d[sa[1]]):
    print('Yes')
    exit()

if n == a.count(0):
  print('Yes')
  exit()

print('No')