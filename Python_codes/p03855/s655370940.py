from collections import*;M=lambda:map(int,input().split());n,k,l=M();d=[-1]*n;t=[-1]*n;r=range
def f(l,x):
  if l[x]<0:return x
  l[x]=f(l,l[x]);return l[x]
def u(l,x,y):
  if f(l,x)!=f(l,y):l[f(l,y)]=f(l,x)
for i in r(k+l):a,b=M();u(d if i<k else t,a-1,b-1)
p=[(f(d,i),f(t,i))for i in r(n)];c=Counter(p);print(*[c[p[i]]for i in r(n)])