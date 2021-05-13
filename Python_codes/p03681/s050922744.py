import math
n,m = map(int,input().split())

if 2 <= abs(n-m):
    print (0)
elif 1 == abs(n-m):
    print ((math.factorial(n)*math.factorial(m))%((10**9)+7))
elif n == m:
    print ((2*(math.factorial(n)*math.factorial(m)))%((10**9)+7))
