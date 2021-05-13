import math

n = int(input())
nn = int(math.sqrt(n))+1

ans = [0] * n
for x in range(1,nn):
    for y in range(1,nn):
        for z in range(1,nn):
            f = x**2+y**2+z**2+x*y+y*z+z*x
            if f <= n:
                ans[f-1] += 1

for a in ans:
    print(a)

