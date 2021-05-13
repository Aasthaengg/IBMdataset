from math import sqrt

S=int(input())
if S==10**18:
    print(10**9,0,0,10**9,0,0)
else:
    q=int(sqrt(S))
    test=q*(q+1)-S
    if test>=0:
        print(0,0,q,1,test,q+1)
    else:
        print(0,1,q+1,0,-test,q+1)