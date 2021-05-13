import math
N = int(input())
T = [int(input()) for _ in range(N)]
 
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
 
ans = 1
 
for i in range(N):
    ans = lcm(ans,T[i])
 
print(ans)