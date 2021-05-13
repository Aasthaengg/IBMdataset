from math import gcd

A,B,C,D=map(int,input().split())

lcm = C*D//gcd(C,D)

def n_mul(c):
  if A%c==0 and B%c==0:return(B//c-A//c+1)
  elif A%c==0 and B%c!=0:return(B//c-A//c+1)
  elif A%c!=0 and B%c==0:return(B//c-A//c)
  else:return(B//c-A//c)

print(B-A+1-(n_mul(C)+n_mul(D)-n_mul(lcm)))