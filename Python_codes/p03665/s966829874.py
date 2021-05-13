import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n,p=map(int,input().split())
a=[int(x)%2 for x in input().split()]
z=a.count(0)
o=a.count(1)
onum=0
if p:
  i=1
  while i<=o:
    onum+=combinations_count(o, i)
    i+=2
else:
  i=0
  while i<=o:
    onum+=combinations_count(o, i)
    i+=2
print((2**z)*onum)