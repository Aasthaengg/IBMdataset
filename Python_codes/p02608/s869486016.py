N = int(input())
import math

ans = [0]*N

def g(x,y,z):
    return x**2+y**2+z**2+x*y+y*z+z*x


for x in range(1,int(math.sqrt(N))+10):
    for y in range(1,int(math.sqrt(N))+10):
        for z in range(1,int(math.sqrt(N))+10):
            if g(x,y,z) <= N:
                ans[g(x,y,z)-1] += 1

for p in range(N):
    print(ans[p])

