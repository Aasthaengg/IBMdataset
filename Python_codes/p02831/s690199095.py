import math
def lcm(a,b):
    print(a * b // math.gcd(a, b))
    
a,b=map(int,input().split())

lcm(a,b)