n,a,b=(int(x) for x in input().split())
c=0
d=[]
def sual(N,A,B):
  l=list('{}'.format(N))
  for y in range(len(l)):
      d.append(int(l[y]))
  e=sum(d)
  d.clear()
  if A<=e<=B:
    return True
  else:
    return False

for x in range(n):
  if sual(x+1,a,b):
    c=c+x+1
print(c)
