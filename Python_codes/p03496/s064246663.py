n=int(input())
a=list(map(int,input().split()))
amin=min(a)
amax=max(a)
imin=a.index(min(a))+1
imax=a.index(max(a))+1
if amin>=0:
  print(n-1)
  for i in range(1,n):
    print("{} {}".format(i,i+1))
  exit()
if amax<=0:
  print(n-1)
  for i in range(1,n):
    print("{} {}".format(n-i+1,n-i))
  exit()
print(2*n-1)
if abs(amin)<=abs(amax):
  for i in range(1,n+1):
    print("{} {}".format(imax,i))
  for i in range(1,n):
    print("{} {}".format(i,i+1))
  exit()
if abs(amin)>=abs(amax):
  for i in range(1,n+1):
    print("{} {}".format(imin,i))
  for i in range(1,n):
    print("{} {}".format(n-i+1,n-i))