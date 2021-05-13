from math import factorial
from itertools import permutations

n=int(input())
np=factorial(n)
p_list=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

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