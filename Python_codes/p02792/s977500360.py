n=int(input())
def func(i,j,m): #m以下の整数で先頭がi末尾がjであるものの個数
  ret=0
  s=len(str(m))
  m0=int(str(m)[0])
  if s==1:
    if i==j and i<=m:
      return 1
    else:
      return 0
  if s==2:
    if 10*i+j<=m:
      return 2 if i==j else 1
    else:
      return 1 if i==j else 0
  if i<m0:
    for si in range(s-1):
      ret+=pow(10,si)
  elif i==m0:
    if j<=int(str(m)[-1]):
      ret+=int(str(m)[1:-1])+1
    else:
      ret+=int(str(m)[1:-1])
    for si in range(s-2):
      ret+=pow(10,si)
  elif i>m0:
    for si in range(s-2):
      ret+=pow(10,si)
  return ret if i!=j else ret+1
ans=0
d={}
for i in range(1,10):
  for j in range(1,10):
    a=func(i,j,n)*func(j,i,n)
    ans+=a
    #if a>0:
    #  print(i,j,func(i,j,n),func(j,i,n))

print(ans)