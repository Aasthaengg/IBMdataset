import math
N = int(input())
T = []

def lcm(x, y):
    gc = math.gcd(x, y)
    ans = (x * y)//gc
    return ans

for i in range(N):
    T.append(int(input()))

    

if len(T) > 2:
    g = lcm(T[0],T[1])
    for i in range(3,N-1):
        g = lcm(g,T[i+1])
    print(g)
elif len(T) == 2:
    g = lcm(T[0],T[1])
    print(g)
else:
    print(T[0])