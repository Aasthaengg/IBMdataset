x=int(input())
def eratosthenes(n):
  l0=list(range(2,n+1))
  l1=[1]*(n+1)
  l1[0]=0
  l1[1]=0
  for li in l0:
    if li>int(n**0.5):
      break
    if l1[li]==1:
      k=2
      while k*li<=n:
        l1[k*li]=0
        k+=1
  ret=[i for i,li in enumerate(l1) if li==1]
  return ret
a=eratosthenes(x)
if x in a:
  print(x)
  exit()
while True:
  flg=True
  for ai in a:
    if x%ai==0:
      flg=False
      break
  if flg:
    print(x)
    exit()
  x+=1
