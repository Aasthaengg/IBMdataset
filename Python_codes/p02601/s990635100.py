ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b,c=nm()
k=ni()

while(True):
  if(b<=a):
    if(k<=0):
      print('No')
      exit()
    b*=2
    k-=1
  else:
    break

while(True):
  if(c<=b):
    if(k<=0):
      print('No')
      exit()
    c*=2
    k-=1
  else:
    break
print('Yes')
