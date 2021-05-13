def isPrime(x):
  """
  xが素数か否か判定する。

  Parameters
  ----------
  x: int
      自然数

  Returns
  -------
      True:素数
      False:素数ではない
  """
  if x<2:
    return False
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      return False
  return True


def sieve(x):
  """
  x以下の自然数が素数が否かを判定する。

  Parameters
  ----------
  x: int
      自然数

  Returns
  -------
  f:list
    True:素数
    False:素数以外
  """
  f=[True]*(x+1)
  f[0],f[1]=False,False

  for i in range(2,len(f)):
    if isPrime(i):
      for j in range(i*2,len(f),i):
        f[j]=False
  return f

n=int(input())
a=sieve(55555)
b=[]
for i,aa in enumerate(a):
  if aa==1:
    if i%5==1:
      b.append(i)
print(*b[:n])
