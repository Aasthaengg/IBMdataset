import math
def lcm(x, y):return (x * y) // math.gcd(x, y)
n = int(input())
a = [int(input()) for i in range(n)]
ans = 1
for i in a:ans = lcm(ans,i)
print(ans)