import math

while True:
    n = input()
    if(n==0):
        break
    l = map(float, raw_input().split())
    varience = sum(map(lambda x: (x - (sum(l)/n))**2 / n, l))
    print math.sqrt(varience)