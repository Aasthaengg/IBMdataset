n=int(input())
a=list(map(int,input().split()))

def cnt(p):
  s=d=0
  for i in range(n):
    c=(s+a[i])*p
    if c<=0:
      d+=(1-c)
      s=p
    else:
      s+=a[i]
    p*=(-1)
  return d

da=cnt(1)
db=cnt(-1)
print(min(da,db))