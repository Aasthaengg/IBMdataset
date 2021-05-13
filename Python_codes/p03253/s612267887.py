N,M=map(int,input().split())
from operator import mul
from functools import reduce
if M==1:
  print(1)
else:
  def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

  def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

  a=factorization(M)
  A=[]
  for i in range(len(a)):
    A.append(a[i][1])
  ans=1
  for i in A:
    d=cmb(i+N-1,i)
    ans*=d%(10**9+7)
  print(ans%(10**9+7))
