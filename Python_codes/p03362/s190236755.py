
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
s=eratosthenes(55555)
ans=['2']
n=int(input())
for si in s:
  if str(si)[-1]=='3':
    ans.append(str(si))
print(' '.join(ans[:n]))
