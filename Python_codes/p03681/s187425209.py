import math
n,m = map(int,input().split())
num = abs(n-m)
if num > 1:
    print(0)
else:
    dum1 = math.factorial(n)
    dum2 = math.factorial(m)
    if num == 1:
        print((dum1*dum2)%(10**9+7))
    else:
        print(((dum1 * dum2))*2 % (10 ** 9 + 7))