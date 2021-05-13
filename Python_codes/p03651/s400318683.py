from collections import deque
import fractions as fr
import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

n ,k= map(int,input().split())
a = tuple(map(int,input().split()))

ans = 0
x=a[0]
for i in range(1,n):
    x =fr.gcd(x,a[i])
    # print(x)
if max(a)<k:
    print("IMPOSSIBLE")
elif k in a:
    print("POSSIBLE")
elif k%x == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
