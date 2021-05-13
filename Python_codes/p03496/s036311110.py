import sys
read=sys.stdin.read

n,*a=map(int,read().split())
def output(x,y):
  #a[y]+=a[x]
  print('{} {}'.format(x+1,y+1))
mx=max(a)
mxi=a.index(mx)
mn=min(a)
mni=a.index(mn)

print(2*n-1)
if abs(mx)>=abs(mn) and mx>=0:
  for i in range(n):
    if mxi!=i:
      output(mxi,i)
  output(mxi,mxi)
  for i in range(1,n):
    output(i-1,i)
elif abs(mx)<abs(mn) and mn<0:
  for i in range(n):
    if mni!=i:
      output(mni,i)
  output(mni,mni)
  for i in range(n-1,0,-1):
    output(i,i-1)