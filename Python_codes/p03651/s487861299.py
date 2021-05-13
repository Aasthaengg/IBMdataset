import sys
N,K=map(int,input().split())
a=list(map(int,input().split()))
def gcd(a,b):
  if a==b:
    return a
  else:
    a,b=max(a,b),min(a,b)
    if a%b==0:
      return b
    else:
      return gcd(b,a%b)
if N==1:
  if K==a[0]:
    print('POSSIBLE')
  else:
    print('IMPOSSIBLE')
  sys.exit()
          
for i in range(N-1):
  if i==0:
    tmp=gcd(a[i],a[i+1])
  else:
    tmp=gcd(tmp,a[i+1])
if tmp==1:
  if K<=max(a):
    print('POSSIBLE')
  else:
    print('IMPOSSIBLE')
else:
  if K<=max(a):
    if K%tmp==0:
      print('POSSIBLE')
    else:
      print('IMPOSSIBLE')
  else:
    print('IMPOSSIBLE')