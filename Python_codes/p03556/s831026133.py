import math
n = int(input())
for i in range(n):
    x = n - i
    if math.sqrt(x).is_integer():
        print (x)
        exit ()
