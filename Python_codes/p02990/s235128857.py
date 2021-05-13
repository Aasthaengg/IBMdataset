n,blue = map(int,input().split())
red = n-blue
MOD = 10**9+7

def cmb(n,r):
    if (n-r)<r: r=n-r
    if r==0: return 1
    if r==1: return n

    numerator = [n-r + k+1 for k in range(r)]
    denominator = [k+1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p-1]
        if pivot>1:
            offset = (n-r)%p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def f(x,y):
  if x==0 and y==0:
    return 1
  elif y==0:
    return 0
  else:
    return cmb(x-1,y-1)

for i in range(blue):
  # 青の並べ方
  ao = f(blue,i+1)

  # 赤の並べ方
  if red<i:
    ak = 0
  elif red==i:
    ak = f(red,i)
  elif red==i+1:
    ak = f(red,i) + f(red,i+1) + f(red,i+1)
  else:
    ak = f(red,i) + f(red,i+1) + f(red,i+1) + f(red,i+2)
  
  print(ao*ak % MOD)