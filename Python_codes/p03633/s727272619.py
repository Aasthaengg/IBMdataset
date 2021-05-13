import math
N = int(input())
T = [int(input()) for _ in range(N)]

def lcm(x, y):
    return (x * y)//math.gcd(x,y)

g = 1
for i in T:
    g = lcm(g,i)
    
print(g)