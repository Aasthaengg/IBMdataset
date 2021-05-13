import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

x,y = map(int,input().split())
if x!=0 and x!=1:
    a = combinations_count(x, 2)
else:
    a=0
if y!=0 and y!=1:
    b = combinations_count(y, 2)
else:
    b=0

print(a+b)