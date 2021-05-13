from math import gcd
from collections import defaultdict
n=int(input())
A=defaultdict(int)
AA=defaultdict(int)
B=[]
C=[]
X=[]
mod=10**9+7
for i in range(n):
  a,b=map(int,input().split())
  if a<0:
    a=a*-1
    b=b*-1
  if a*b>0:
    l=a*b//gcd(a,b)
    A[str(l//b)+":"+str(l//a)]+=1
  elif a*b<0:
    l=a*(-b)//gcd(a,-b)
    AA[str(l//a)+":"+str(l//(-b))]+=1
  else:
    if a==0 and b==0:
      X.append(i)
    elif a==0:
      B.append(i)
    else:
      C.append(i)
E=set(list(A.keys())+list(AA.keys()))
a=1
for i in E:
  a=(a*(2**A[i]+2**AA[i]-1))%mod
a=(a*(2**len(B)+2**len(C)-1)-1)%mod
print((a+len(X))%mod)