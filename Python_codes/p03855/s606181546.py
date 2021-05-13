from collections import *;M=lambda:map(int,input().split());r=range;n,k,l=M()
def f(m):
 *a,=r(n)
 def g(i):
  if a[i]==i:return i
  a[i]=g(a[i]);return a[i]
 for _ in r(m):p,q=M();a[g(q-1)]=g(p-1)
 return [g(i) for i in r(n)]
z=[*zip(f(k),f(l))];c=Counter(z);print(*(c[x]for x in z))