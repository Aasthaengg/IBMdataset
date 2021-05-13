from math import ceil
S=int(input())
 
if S<=10**9:
  d=0
  c=S
else:
  d=ceil (S/(10**9))
  c=10**9*d-S
 
print(0,0,10**9,1,c,d)