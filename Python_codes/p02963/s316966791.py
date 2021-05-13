import math 
s=int(input())
if s<=10**9:
    print(0,0,1,0,0,s)
else:
    b=int(math.ceil(s/10**9))
    a=10**9*b-s
    print(0,0,10**9,1,a,b)