from collections import defaultdict
import math
import sys
input=sys.stdin.readline
MOD=10**9+7
N=int(input())

def powmod(a,p):
  if p==0:
    return 1
  else:
    pow2=powmod(a,p//2)
    if p%2==0:
      return (pow2**2)%MOD
    else:
      return (a*pow2**2)%MOD

ratio_dic=defaultdict(int)
zero2_num=0

for i in range(N):
  A,B=map(int,input().split())
  if A==0 and B==0:
    zero2_num+=1
  elif A==0:
    ratio_dic[(0,1)]+=1
  elif B==0:
    ratio_dic[(1,0)]+=1
  elif B>0:
    AB_gcd=math.gcd(A,B)
    Arat=A//AB_gcd
    Brat=B//AB_gcd
    #print(A,B,Arat,Brat)
    ratio_dic[(Arat,Brat)]+=1
  else:
    AB_gcd=math.gcd(A,B)
    Arat=-A//AB_gcd
    Brat=-B//AB_gcd    
    #print(A,B,Arat,Brat)
    ratio_dic[(Arat,Brat)]+=1
#print(zero2_num,ratio_dic)

answer=1
checked_set=set()
for k,v in list(ratio_dic.items()):
  if k in checked_set:
    continue
  
  a,b=k
  #(a,b)<=>(ainv,binv)
  if a>0:
    ainv,binv=-b,a
  else:
    ainv,binv=b,-a
    
  num_k1=ratio_dic[(a,b)]
  num_k2=ratio_dic[(ainv,binv)]
  answer*=powmod(2,num_k1)+powmod(2,num_k2)-1
  answer%=MOD
  #print(k,(ainv,binv),num_k1,num_k2)
  
  checked_set.add((a,b))
  checked_set.add((ainv,binv))
  
print((zero2_num+answer-1)%MOD)