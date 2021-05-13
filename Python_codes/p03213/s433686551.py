from math import factorial
from itertools import permutations

n=int(input())

np=factorial(n)

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

lim=10**2+1
is_p, p_list=eratosthenes(lim)

cnt=0
ans=[]
l=len(p_list)
for i in range(l):
  for j in range(i+1,l):
    for k in range(j+1,l):
      for s,t,u in permutations([p_list[i],p_list[j],p_list[k]],3):
        num1=(s**4)*(t**4)*(u**2)
        num2=(s**14)*(t**4)
        num3=(s**24)*(t**2)
        num4=s**74
        for z in [num1,num2,num3,num4]:
          if np%z==0:
            ans.append(z)

print(len(set(ans)))