import itertools
n,l=int(input()),list(input().split())
g=itertools.groupby(l)
c=0
for key,group in g:
  gr=list(group)
  if len(gr)!=1:
    c+=len(gr)//2
print(c)