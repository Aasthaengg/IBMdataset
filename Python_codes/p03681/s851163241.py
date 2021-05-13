import math
n,m=map(int,input().split())
dog = math.factorial(n)
monkey = math.factorial(m)
ans = dog*monkey%(10**9+7)
if abs(n-m)==0:
    print(ans*2%(10**9+7))
elif abs(n-m)==1:
    print(ans%(10**9+7))
else:
    print(0)