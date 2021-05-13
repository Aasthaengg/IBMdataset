import numpy as np

N,A,B=[int(i) for i in input().split()]
x=min(A,B)
if((A+B)>N):
    z=N
    y=abs(A+B-z)
else:
    y=0
print("{} {}".format(x,y))
