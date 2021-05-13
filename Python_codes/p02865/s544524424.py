import math

N = int(input())

if N % 2 == 0 :
    num = N/2 - 1
    print (math.floor(num))
else :
    num = N/2
    print (math.floor(num))