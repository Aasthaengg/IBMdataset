import math
K,A,B=map(int,input().split())

if B-A>1:
    if K<=A:
        print(K+1)
    else:
        print((B-A)*max(0,math.floor((K-(A-1))/2))+A+1-((K+A)%2))
else:   #B-A<=0
    print(1+K)
