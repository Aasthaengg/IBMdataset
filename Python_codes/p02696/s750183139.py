import math
a,b,n = map(int,input().split())
if b-1 <= n:
    print(math.floor((a*(b-1))/b)-(a*math.floor((b-1)/b)))
else:
    print(math.floor((a * (n)) / b) - (a * math.floor((n) / b)))