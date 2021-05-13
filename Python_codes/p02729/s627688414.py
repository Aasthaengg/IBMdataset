import math
N,M=(map(int,input().split()))
a=0
if N>=2:
    x=math.factorial(N)/(math.factorial(N-2)*2)
    a=a+x
if M>=2:
    y=math.factorial(M)/(math.factorial(M-2)*2)
    a=a+y
if a!=0:
    print(int(a))
else:
    print('0')