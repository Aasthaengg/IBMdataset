from math import factorial
from itertools import permutations

def eratosthenes(n):
 is_p=[1]*n
 p_list=[]

 is_p[0]=0
 is_p[1]=0

 for i in range(2,n):
  if is_p[i]:
   p_list.append(i)
   for j in range(i*i,n,i):
    is_p[j] = 0

 return is_p, p_list

n=int(input())
np=factorial(n)

lim=10**2+1
is_p, p_list=eratosthenes(lim)

ans=[]
for s,t,u in permutations(p_list,3):
  num1=(s**4)*(t**4)*(u**2)
  num2=(s**14)*(t**4)
  num3=(s**24)*(t**2)
  num4=s**74
  for z in [num1,num2,num3,num4]:
    if np%z==0:
      ans.append(z)

print(len(set(ans)))