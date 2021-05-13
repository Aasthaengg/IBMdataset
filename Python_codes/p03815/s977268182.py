import math
n = int(input())
q = math.floor(n/11)
r = n % 11
if r == 0: print(2*q)
elif r <= 6: print(2*q+1)
else: print(2*q+2)